import pyautogui#여러 지역 날씨를 자동으로 검색 후 저장하는 코드 만들기
import time
import pyperclip

날씨=["서울날씨","관악구날씨","여의도날씨","여수날씨","부산날씨"]

addr_x=300
addr_y=88
start_x=310
start_y=340
end_x=1028
end_y=1431

for 지역날씨 in 날씨:
  pyautogui.moveTo(addr_x,addr_y,1)
  time.sleep(1)
  pyautogui.click()
  time.sleep(.2)
  pyautogui.typewrite(["www.naver.com"],interval=0.1)#주소를 .1초간격으으로 영문 입력
  pyautogui.write(["enter"])
  time.sleep(1)

  pyperclip.copy(지역날씨)
  pyautogui.hotkey("ctrl","v")
  time.sleep(0.5)
  pyautogui.write(["enter"])
  time.sleep(1)
  저장경로='10. 오토마우스를 활용한 웹페이지 자동화\\'+지역날씨+'.png'
  pyautogui.screenshot(저장경로,region=(start_x,start_y,end_x,end_y))