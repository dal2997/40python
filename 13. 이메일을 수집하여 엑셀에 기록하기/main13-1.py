import re #정규표현식을 사용하기 위해 re 모듈을 불러옵니다.

test_string= """ 3~11 테스트 용도로 사용할 문자열을 생성합니다. 문자열 여러 개를 입력하기 위하여 쌍따옴표3번으로 시작하고,종료함.따옴표3개도 가능함.
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

results=re.findall(r'[\w\.-]+@[\w\.-]+', test_string)#문자열에서 이메일 형식을 찾아 리스트형태로 결과를 반환합니다.

print(results)#찾은 이메일 주소를 출력합니다.