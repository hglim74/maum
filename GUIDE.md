# Mind Connect (마음커넥트) 실행 가이드

이 문서는 Mind Connect AI 심리상담 서비스를 로컬 환경에서 실행하거나 구글 클라우드에 배포하는 방법을 설명합니다.

## 1. 프로젝트 구조 개요
- **core/**: 도메인 엔티티 및 비즈니스 로직 (Clean Architecture)
- **infrastructure/**: 외부 인터페이스 어댑터 및 프레임워크 (FastAPI, Static Files)
- **deploy/**: Docker 및 Google Cloud Build 설정
- **requirements.txt**: 파이썬 의존성 패키지 목록

## 2. 로컬 개발 환경 실행 방법

### 필수 조건
- Python 3.10 이상 설치
- pip (파이썬 패키지 관리자)

### 실행 순서
1. **의존성 설치**
   ```bash
   pip install -r requirements.txt
   ```

2. **서버 실행**
   프로젝트 루트 디렉토리에서 아래 명령어를 실행합니다:
   ```bash
   python -m infrastructure.frameworks.web.main
   ```
   또는 `uvicorn`을 직접 사용:
   ```bash
   uvicorn infrastructure.frameworks.web.main:app --reload --port 8000
   ```

3. **웹 접속**
   브라우저를 열고 `http://localhost:8000`에 접속합니다.

## 3. Docker를 이용한 실행

### 실행 순서
1. **이미지 빌드**
   ```bash
   docker build -t mind-connect -f deploy/Dockerfile .
   ```

2. **컨테이너 실행**
   ```bash
   docker run -p 8080:8080 mind-connect
   ```

3. **접속**
   브라우저에서 `http://localhost:8080`으로 접속합니다.

## 4. 구글 클라우드 배포 (Cloud Run)

1. **Google Cloud SDK**가 설치되어 있고 프로젝트가 설정되어 있어야 합니다.
2. 아래 명령어를 사용하여 Cloud Build를 통해 배포를 진행합니다:
   ```bash
   gcloud builds submit --config deploy/cloudbuild.yaml .
   ```

## 5. 주요 API 엔드포인트
- `POST /counseling/start`: 상담 세션 시작 및 웰컴 메시지 생성
- `POST /counseling/chat`: 사용자 메시지 전송 및 AI 공감 답변 수신
- `POST /counseling/finish`: 상담 종료 및 마음 리포트 생성
- `GET /history/{user_id}`: 특정 사용자의 상담 히스토리 조회

---
**주의**: 현재 AI 게이트웨이는 Mock 형태로 구현되어 있습니다. 실제 Gemini API 연동을 위해서는 `infrastructure/adapters/gateways/gemini_client.py`에서 API 키 설정 및 클라이언트 라이브러리 연동이 필요합니다.
