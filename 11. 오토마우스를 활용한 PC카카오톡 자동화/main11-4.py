import pyautogui
import pyperclip
import time
import threading
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def send_message():
  threading.Timer(10, send_message).start()

  picPosition=pyautogui.locateOnScreen('pic1.png')
  print(picPosition)

  if picPosition is None:
    picPosition=pyautogui.locateOnScreen('pic2.png')
    print(picPosition)

  if picPosition is None:
    picPosition=pyautogui.locateOnScreen('pic3.png')
    print(picPosition)

  clickPosition=pyautogui.center(picPosition)
  pyautogui.doubleClick(clickPosition)

  pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다.")
  pyautogui.hotkey("ctrl","v")
  time.sleep(1.0)

  pyautogui.write(["enter"])
  time.sleep(1.0)

# 스케줄 이용
# 스케줄을 이용하면 다음과 같이 설정도 가능합니다.
# 30분마다 실행
# schedule.every(30).minutes.do(실행할 함수)

# 매주 월요일 9시 10분마다 실행
# schedule.every().monday.at("09:10").do(실행할 함수)

# 매일 10시 30분마다 실행
# schedule.every().day.at("10:30")