import pyautogui
import pyperclip
import time
import os

#경로를 .py 파일의 실행 경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition=pyautogui.locateOnScreen('pic1.png')
print(picPosition)

if picPosition is None:#10~12: 앞에 사진에서 좌표를 찾지 못하였다면 pic2.png 파일과 동일한 그림을 찾아 좌표를 출력합니다.
  time.sleep(1)
  picPosition=pyautogui.locateOnScreen('pic2.png')
  print(picPosition)

if picPosition is None:#14~16: 앞에 사진에서 좌표를 찾지 못하였다면 pic3.png 파일과 동일한 그림을 찾아 좌표를 출력합니다.
  time.sleep(1)
  picPosition=pyautogui.locateOnScreen('pic3.png')
  print(picPosition)

clickPosition=pyautogui.center(picPosition)#앞서 찾은 이미지의 좌표 중간값 좌표값을 찾습니다.
pyautogui.doubleClick(clickPosition)

pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다.")
pyautogui.hotkey("ctrl","v")
time.sleep(1.0)

pyautogui.write(["enter"])
time.sleep(1.0)

pyautogui.write(["escape"])
time.sleep(1.0)

