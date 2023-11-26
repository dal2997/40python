from gtts import gTTS
from playsound import playsound
import os

#경로를 .py파일의 실행경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path='나의 텍스트.txt'# 나의 텍스트.txt 경로를 바인딩해야함.
with open(file_path, 'rt', encoding='UTF8')as f:#파일을 f의 이름으로 오픈합니다. 한글로 작성된 파일을 열기 때문에 'rt'.encoding='UTF8'형식으로 열어 글자가 깨지지 않게 함.
  read_file=f.read()#파일의 전체 내용을 읽어 read_file변수에 바인딩함.

tts = gTTS(text=read_file, lang='ko')#with는 파일을 열고 종료되면 자동으로 파일을 닫습니다. 파일을 열때 with를 사용하면 코드가 간결해 집니다.

tts.save("myText.mp3")#[myText.mp3]파일을 생성하고 음성으로 출력합니다.