import socket
import requests
import re

#ModuleNotFoundError: No module named 'requests' 오류 메시지가 표시된다면 Python 유틸리티 pip를 사용하여 추가 모듈(requests)을 설치합니다.
#terminal을 키고, pip install requests를 치기.

in_addr=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("내부 IP: ",in_addr.getsockname()[0])

req=requests.get("http://ipconfig.kr")
out_addr=re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: ",out_addr)