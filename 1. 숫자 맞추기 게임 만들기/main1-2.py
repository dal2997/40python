'''random 함수의 기능들
random.random() 
0.0에서부터 0.999999 사이의 실수를 반환합니다.
random.uniform(a,b)
a와 b사이의 실수값을 반환합니다.
random.randint(a,b)
a와 b사이의 정수값을 반환합니다.
random.randrange(a,b)
a와 b사이의 정수값을 반환합니다.
random.randrange(a)
인자가 하나일 경우 0부터 a사이의 정수값을 반환합니다.
random.choice(type)
type에는 문자열, 리스트, 튜플, range의 값을 입력받을 수 있고 무작위로 하나의 원소를 뽑습니다.
'''

import random
random_number=random.randint(1,100)
# print(random_number)

game_count=1

while True:
  my_number=int(input("1~100 사이의 숫자를 입력하세요:"))
  if my_number>random_number:
    print("다운")
  elif my_number<random_number:
    print("업")
  elif my_number==random_number:
    print(f"축하합니다.{game_count}회 만에 맞췄습니다.")
    break
  game_count=game_count+1

  