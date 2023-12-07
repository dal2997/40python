import pyautogui
import time
import pyperclip

pyautogui.moveTo(1241,206,0.2)#네이버의 검색창의 좌표로 .2초 동안 이동합니다.
pyautogui.click()#마우스를 클릭합니다.
time.sleep(0.5)#.5초 기다립니다.

pyperclip.copy("서울 날씨")#클립보드에 "서울날씨"를 저장합니다.
pyautogui.hotkey("ctrl","v")#클립보드에 저장된 내용을 붙여넣기 합니다. [ctrl v]키를 입력합니다.
time.sleep(0.5)#.5초 기다립니다.

pyautogui.write(["enter"])#엔터키를 입력합니다.
time.sleep(1)#1초동안 기다립니다.