from gtts import gTTS
from playsound import playsound #playsound모듈로부터 playsound를 불러와 사용합니다.
import os#경로를 이동하기 위해서 os라이브러리를 불러옵니다.

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))#경로를 현제.py파일을 실행하는 경로로 이동합니다. playsound에서 한글을 인식하지 못하여 경로를 이동하였습니다. 

text="안녕하세요. 파이썬과 40개의 작품들 입니다."

tts=gTTS(text=text, lang="ko")
tts.save("hi.mp3")

playsound("hi.mp3")