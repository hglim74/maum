FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8080

# Environment variables
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

# Run the application using the sh -c wrapper to handle the PORT env var
CMD ["sh", "-c", "uvicorn infrastructure.frameworks.web.main:app --host 0.0.0.0 --port ${PORT:-8080}"]