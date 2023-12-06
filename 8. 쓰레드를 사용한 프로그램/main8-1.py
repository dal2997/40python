import threading#쓰레드를 사용하기 위하여 threading 모듈을 불러옵니다.
import time

def thread_1():#thread_1의 함수로 1초마다 "쓰레드1동작"을 출력합니다.
  while True:
    print("쓰레드1 동작")
    time.sleep(1.0)

t1=threading.Thread(target=thread_1)#쓰레드를 설정합니다.
t1.start()#쓰레드를 시작합니다.

while True:#12-13:메인코드로 "메인동작"을 2초마다 출력합니다.
  print("메인동작")
  time.sleep(2.0)

  #쓰레드란 코드를 실행하는 하나의 동작입니다. 우리는 파이썬 코드를 이용하여 하나의 동작을 하는 코드를 만들고 잇습니다.
  #하지만 프로그램이 커지고 해야 할 일이 많아진다면 하나의 동작만을 가지고는 부족하여 쓰레드라는 방식의 프로그램 방식을 사용하여 동작을 늘릴 수 있습니다.

# # 2가지 동작이 동시에 실행되는 코드 만들고 실행 # #