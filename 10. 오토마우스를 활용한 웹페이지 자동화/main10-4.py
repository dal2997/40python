import pyautogui#여러 지역 날씨를 자동으로 검색 후 저장하는 코드 만들기
import time
import pyperclip

날씨=["서울날씨","관악구날씨","여의도날씨","여수날씨","부산날씨"]#검색하고 싶은 지역을 리스트 형태로 입력합니다.

addr_x=300#웹 브라우저의주소창의 좌표 x값입니다.
addr_y=88#웹 브라우저의 주소창의 좌표 y값입니다.
start_x=310#9~12 스크린 캡쳐를 위한 좌표값입니다.
start_y=340
end_x=1028
end_y=1431

for 지역날씨 in 날씨:#14~29 날씨 변수의 수만큼 반복합니다.
  pyautogui.moveTo(addr_x,addr_y,1)#검색창의 주소 좌표로 1초에 걸쳐서 이동합니다.
  time.sleep(1)
  pyautogui.click()
  time.sleep(.2)
  pyautogui.typewrite(["www.naver.com"],interval=0.1)#주소를 .1초간격으으로 영문 입력합니다.
  pyautogui.write(["enter"])
  time.sleep(1)

  pyperclip.copy(지역날씨)
  pyautogui.hotkey("ctrl","v")
  time.sleep(0.5)
  pyautogui.write(["enter"])
  time.sleep(1)
  저장경로='10. 오토마우스를 활용한 웹페이지 자동화\\'+지역날씨+'.png'#저장할 경로와 파일명을 지정해줍니다.
  pyautogui.screenshot(저장경로,region=(start_x,start_y,end_x,end_y))#스크린 캡처하여 저장합니다.관악구날씨
  