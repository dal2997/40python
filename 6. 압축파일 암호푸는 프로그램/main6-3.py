import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile):#un_zip의 이름으로 함수와 하였습니다. 입력값으로 패스워드 문자열, 비밀번호 최소길이, 비밀번호 최대길이 ,
  for len in range(min_len, max_len+1):
    to_attempt=itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
      passwd=''.join(attempt)
      print(passwd)
      try:
        zFile.extractall(pwd=passwd.encode())
        print(f"비밀번호는 {passwd} 입니다.")
        return 1
      except:
        pass

passwd_string="0123456789"

zFile=zipfile.ZipFile(r'6. 압축파일 암호푸는 프로그램\암호1234.zip')

min_len=1
max_len=5

unzip_result=un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result ==1:
  print("암호찾기에 성공하였습니다.")
  print("암호찾기에 실패하였습니다.")