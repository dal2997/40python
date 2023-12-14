import re

test_string="""
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

results=re.findall(r'[\w\.-]+@[\w\.-]+', test_string)

results= list(set(results)) #set을 사용하여 중복을 제거합니다.

print(results)