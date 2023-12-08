import pyautogui
import os
import time

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))# 경로를 현재 .py파일을 실행하는 경로로 이동합니다. pyautogui에서 한글을 인식하지 못하여 경로를 이동하였습니다.
time.sleep(1)
picPosition=pyautogui.locateOnScreen('pic1.png')#7~8: pic1.png 파일과 동일한 그림을 찾아 좌표를 출력합니다.
print(picPosition)

if picPosition is None:#10~12: 앞에 사진에서 좌표를 찾지 못하였다면 pic2.png 파일과 동일한 그림을 찾아 좌표를 출력합니다.
  time.sleep(1)
  picPosition=pyautogui.locateOnScreen('pic2.png')
  print(picPosition)

if picPosition is None:#14~16: 앞에 사진에서 좌표를 찾지 못하였다면 pic3.png 파일과 동일한 그림을 찾아 좌표를 출력합니다.
  time.sleep(1)
  picPosition=pyautogui.locateOnScreen('pic3.png')
  print(picPosition)

#주의사항은 pic1,pic2,pic3이 이미지 그대로여야 인식함.. 창의 크기도 유의해야함...
#pic1.png좌표: left=2671, top=654, width=468, height=94