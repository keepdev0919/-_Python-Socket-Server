#!/bin/bash

# 실습과제 3 테스트용 curl 스크립트
# 서버가 실행 중일 때 이 스크립트를 실행하여 테스트

echo "=== Python Socket Server 테스트 ==="
echo "서버가 http://127.0.0.1:8000 에서 실행 중인지 확인하세요."
echo ""

# 테스트용 이미지 파일 확인
IMAGE_FILE="images/Cat Working GIF.gif"
if [ ! -f "$IMAGE_FILE" ]; then
    echo "이미지 파일을 찾을 수 없습니다: $IMAGE_FILE"
    echo "images/ 폴더에 이미지 파일을 준비해주세요."
    exit 1
fi
echo "사용할 이미지 파일: $IMAGE_FILE"

echo "curl 요청을 전송합니다..."
echo ""

# curl 요청 실행 (Cat Working GIF 사용)
curl -X POST -S -H "Authorization: JWT b181ce4155b7413ebd1d86f1379151a7e035f8bd" \
-F "author=1" -H 'Accept: application/json' \
-F "title=curl 테스트 - Cat Working GIF" \
-F "text=API curl로 작성된 AP 테스트 입력 입니다. (GIF 이미지 테스트)" \
-F "created_date=2024-06-10T18:34:00+09:00" \
-F "published_date=2024-06-10T18:34:00+09:00" \
-F "image=@$IMAGE_FILE;type=image/gif" \
http://127.0.0.1:8000/api_root/Post/

echo ""
echo ""
echo "=== 테스트 완료 ==="
echo "다음 폴더들을 확인하세요:"
echo "- request/ : 바이너리 요청 파일들"
echo "- images/ : 추출된 이미지 파일들"
