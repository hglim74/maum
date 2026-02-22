const state = {
    userId: 'user123',
    sessionId: null,
    messages: []
};

// View management
function showView(viewId) {
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    document.getElementById(viewId).classList.add('active');
}

// API Helpers
async function apiPost(endpoint, body) {
    const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
    });
    return response.json();
}

async function apiGet(endpoint) {
    const response = await fetch(endpoint);
    return response.json();
}

// UI Helpers
function appendMessage(sender, text) {
    const chatMsgs = document.getElementById('chat-messages');
    const msgDiv = document.createElement('div');
    msgDiv.className = `msg ${sender}`;
    msgDiv.textContent = text;
    chatMsgs.appendChild(msgDiv);
    chatMsgs.scrollTop = chatMsgs.scrollHeight;
}

// Actions
async function startCounseling() {
    const result = await apiPost('/counseling/start', { user_id: state.userId });
    if (result.session_id) {
        state.sessionId = result.session_id;
        showView('counseling');
        appendMessage('ai', result.welcome_message);
    }
}

async function sendMessage() {
    const input = document.getElementById('chat-input');
    const text = input.value.trim();
    if (!text) return;

    appendMessage('user', text);
    input.value = '';
    
    document.querySelector('.typing-indicator').classList.remove('hidden');

    const result = await apiPost('/counseling/chat', {
        session_id: state.sessionId,
        user_id: state.userId,
        text: text
    });

    document.querySelector('.typing-indicator').classList.add('hidden');
    
    if (result.ai_response) {
        appendMessage('ai', result.ai_response);
    }
}

async function finishCounseling() {
    const result = await apiPost('/counseling/finish', { session_id: state.sessionId });
    if (result.report_id) {
        document.getElementById('report-summary').textContent = result.summary;
        // Mock graph representation
        document.getElementById('graph-container').innerHTML = 
            `<div style="height: 10px; width: 100%; background: #dfe6e9; border-radius: 5px; overflow: hidden;">
                <div style="height: 100%; width: 70%; background: #6c5ce7;"></div>
            </div>`;
        showView('report');
    }
}

async function loadHistory() {
    const result = await apiGet(`/history/${state.userId}`);
    const list = document.getElementById('history-list');
    list.innerHTML = '';
    if (result.history) {
        result.history.forEach(item => {
            const div = document.createElement('div');
            div.className = 'card report-card';
            div.innerHTML = `<h4>세션: ${item.session_id}</h4><p>${item.summary}</p>`;
            list.appendChild(div);
        });
    }
    showView('history');
}

// Event Listeners
document.getElementById('start-btn').addEventListener('click', startCounseling);
document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('finish-btn').addEventListener('click', finishCounseling);
document.getElementById('to-history-btn').addEventListener('click', loadHistory);
document.getElementById('to-home-btn').addEventListener('click', () => showView('home'));
document.querySelector('.back-btn-home').addEventListener('click', () => showView('home'));
document.querySelector('.back-btn').addEventListener('click', () => showView('home'));

document.getElementById('chat-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});
