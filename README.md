# 실습과제 3: Python Socket Server

## 과제 개요
Python을 사용하여 Socket Server를 구현하고, 클라이언트 요청을 처리하는 과제입니다.

## 구현 기능

### Practice 1: 바이너리 요청 저장
- 클라이언트 요청을 바이너리 파일로 저장
- 파일명 형식: `year-month-day-hour-minute-second.bin`
- 저장 위치: `request/` 폴더

### Practice 2: 이미지 데이터 저장
- multipart/form-data 요청에서 이미지 데이터 추출
- 이미지 파일을 별도로 저장
- 저장 위치: `images/` 폴더

## 파일 구조
```
실습과제 3/
├── socket_server.py    # 메인 서버 코드
├── README.md          # 이 파일
├── test_curl.sh       # 테스트용 curl 스크립트
├── request/           # 바이너리 요청 파일 저장 폴더
└── images/            # 이미지 파일 저장 폴더
```

## 사용 방법

### 1. 서버 실행
```bash
python3 socket_server.py
```

### 2. 클라이언트 테스트 (curl 사용)
```bash
# 테스트 스크립트 실행
chmod +x test_curl.sh
./test_curl.sh
```

또는 직접 curl 명령어 실행:
```bash
curl -X POST -S -H "Authorization: JWT b181ce4155b7413ebd1d86f1379151a7e035f8bd" \
-F "author=1" -H 'Accept: application/json' \
-F "title=curl 테스트" \
-F "text=API curl로 작성된 AP 테스트 입력 입니다." \
-F "created_date=2024-06-10T18:34:00+09:00" \
-F "published_date=2024-06-10T18:34:00+09:00" \
-F "image=@test_image.jpg;type=image/jpg" \
http://127.0.0.1:8000/api_root/Post/
```

## 출력 파일
- `request/` 폴더: 클라이언트 요청 바이너리 파일들
- `images/` 폴더: 추출된 이미지 파일들

## 요구사항
- Python 3.6 이상
- curl (테스트용)

## 개발자
- 과제: 실습과제 3
- 날짜: 2024년 10월
