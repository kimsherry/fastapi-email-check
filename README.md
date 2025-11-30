# Email Check API

**FastAPI** 기반의 간단한 **REST API**로, 이메일 주소 형식 검증, 차단 도메인 관리, 요청 로그 기록 기능을 제공합니다.  
API 학습용이나 다른 서비스에 통합하기 좋습니다.

---

## 기능

>이메일 형식 검증
> 특정 도메인 차단 (스팸, 임시 이메일 등)
> 요청 로그 기록 (IP, 이메일, 결과, 타임스탬프)
> 가볍고 로컬 실행 가능

---

## 설치 방법

### 1. 저장소 생성

'''
  git clone https://github.com/username/email-check-api.git
  cd email-validator-api
'''

### 2. 가상환경 생성 (선택 사항)

'''
  python -m venv env
  source env/bin/activate  # Linux / MacOS
  env\Scripts\activate     # Windows
'''

### 3. 패키지 설치

'''
  pip install -r requirements.txt
'''

---

## 사용방법

### API 서버에서 실행

'''
  uvicorn app.main:app --reload
'''

---

## API 엔드포인트

### 요청
입력한 이메일이 올바른 형식인지, 차단 도메인인지 확인합니다.

'''
  GET /validate/email?value=<email>
'''

---

## 사용 예시

### 정상이메일

'''
  GET /validate/email?value=test@unji.com
'''
### 응답:
'''
  {
  "valid": true,
  "reason": "ok"
}
'''

### 차단 도메인
'''
  GET /validate/email?value=user@test.com
'''
### 응답:
'''
{
  "valid": false,
  "reason": "blocked domain"
}
'''

### 잘못된형식

'''
  GET /validate/email?value=invalid-email
'''

### 응답:
'''
{
  "valid": false,
  "reason": "invalid format"
}
'''




