#!/bin/bash

# 실습과제 3 테스트용 curl 스크립트
# 서버가 실행 중일 때 이 스크립트를 실행하여 테스트

echo "=== Python Socket Server 테스트 ==="
echo "서버가 http://127.0.0.1:8000 에서 실행 중인지 확인하세요."
echo ""

# 테스트용 이미지 파일이 있는지 확인
if [ ! -f "test_image.jpg" ]; then
    echo "테스트용 이미지 파일을 생성합니다..."
    # 간단한 테스트 이미지 생성 (1x1 픽셀 PNG)
    python3 -c "
from PIL import Image
import os
img = Image.new('RGB', (100, 100), color='red')
img.save('test_image.jpg', 'JPEG')
print('테스트 이미지 생성 완료: test_image.jpg')
" 2>/dev/null || echo "PIL이 없어서 이미지 생성에 실패했습니다. 직접 test_image.jpg 파일을 준비해주세요."
fi

echo "curl 요청을 전송합니다..."
echo ""

# curl 요청 실행 (강의 자료와 동일한 형식)
curl -X POST -S -H "Authorization: JWT b181ce4155b7413ebd1d86f1379151a7e035f8bd" \
-F "author=1" -H 'Accept: application/json' \
-F "title=curl 테스트" \
-F "text=API curl로 작성된 AP 테스트 입력 입니다." \
-F "created_date=2024-06-10T18:34:00+09:00" \
-F "published_date=2024-06-10T18:34:00+09:00" \
-F "image=@test_image.jpg;type=image/jpg" \
http://127.0.0.1:8000/api_root/Post/

echo ""
echo ""
echo "=== 테스트 완료 ==="
echo "다음 폴더들을 확인하세요:"
echo "- request/ : 바이너리 요청 파일들"
echo "- images/ : 추출된 이미지 파일들"
