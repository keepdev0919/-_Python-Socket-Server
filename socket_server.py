#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Socket Server for 실습과제 3
클라이언트 요청을 받아 바이너리 파일로 저장하고, 
multipart 요청의 이미지 데이터를 별도 파일로 저장하는 서버
"""

import os
import socket
import datetime

class SocketServer:
    """HTTP 요청을 처리하는 Socket Server 클래스"""
    
    def __init__(self):
        """서버 초기화"""
        self.bufsize = 1024
        
        # 응답 파일 읽기
        try:
            with open('./response.bin', 'rb') as f:
                self.RESPONSE = f.read()
        except FileNotFoundError:
            # response.bin이 없을 경우 기본 응답 생성
            self.RESPONSE = b"""HTTP/1.1 200 OK
Server:socket server v0.1
Content-Type: text/plain

<html>
<head>
<title>socketserver</title>
</head>
<body>I've got your message</body>
</html>"""
        
        # 요청 저장 디렉토리 경로
        self.DIR_PATH = './request'
        self.createDir(self.DIR_PATH)
        
        # 이미지 저장 디렉토리
        self.IMAGE_DIR = './images'
        self.createDir(self.IMAGE_DIR)
    
    def createDir(self, path):
        """디렉토리 생성"""
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"디렉토리 생성: {path}")
        except OSError:
            print("Error: Failed to create the directory.")
    
    def run(self, ip, port):
        """서버 실행"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((ip, port))
        self.sock.listen(10)
        
        print(f"서버 시작: http://{ip}:{port}")
        print("서버를 중지하려면 Ctrl+C를 누르세요.")
        
        try:
            while True:
                clnt_sock, req_addr = self.sock.accept()
                clnt_sock.settimeout(5.0)
                print("Request message...\r\n")
                
                # 클라이언트 요청 데이터 수신
                request_data = b""
                while True:
                    try:
                        chunk = clnt_sock.recv(self.bufsize)
                        if not chunk:
                            break
                        request_data += chunk
                    except socket.timeout:
                        break
                
                if request_data:
                    # Practice 1: 클라이언트 요청을 바이너리 파일로 저장
                    now = datetime.datetime.now()
                    filename = now.strftime("%Y-%m-%d-%H-%M-%S.bin")
                    filepath = os.path.join(self.DIR_PATH, filename)
                    
                    with open(filepath, 'wb') as f:
                        f.write(request_data)
                    print(f"바이너리 요청 저장: {filepath}")
                    
                    # Practice 2: multipart 요청에서 이미지 데이터 추출
                    self._extract_images(request_data)
                
                # 응답 전송
                clnt_sock.sendall(self.RESPONSE)
                clnt_sock.close()
                
        except KeyboardInterrupt:
            print("\n서버 종료 중...")
        finally:
            self.sock.close()
    
    def _extract_images(self, request_data):
        """multipart 요청에서 이미지 데이터 추출 및 저장"""
        try:
            request_str = request_data.decode('utf-8', errors='ignore')
            
            if 'multipart/form-data' in request_str:
                # boundary 추출
                import re
                boundary_match = re.search(r'boundary=([^;\r\n]+)', request_str)
                if boundary_match:
                    boundary = boundary_match.group(1)
                    print(f"Multipart boundary: {boundary}")
                    
                    # multipart 데이터 파싱
                    parts = request_data.split(f'--{boundary}'.encode())
                    
                    for part in parts:
                        if b'Content-Disposition: form-data' in part and b'name="image"' in part:
                            # 헤더와 본문 분리
                            if b'\r\n\r\n' in part:
                                header, body = part.split(b'\r\n\r\n', 1)
                                
                                # 파일명 추출
                                filename_match = re.search(rb'filename="([^"]+)"', header)
                                if filename_match:
                                    filename = filename_match.group(1).decode('utf-8')
                                    
                                    # 이미지 데이터 저장
                                    image_path = os.path.join(self.IMAGE_DIR, filename)
                                    with open(image_path, 'wb') as f:
                                        # multipart 데이터 끝부분 정리
                                        image_data = body.rstrip(b'\r\n--')
                                        f.write(image_data)
                                    
                                    print(f"이미지 저장 완료: {image_path}")
                                    
        except Exception as e:
            print(f"이미지 추출 중 오류: {e}")

if __name__ == "__main__":
    server = SocketServer()
    server.run("127.0.0.1", 8000)
