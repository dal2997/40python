from os import linesep
import googletrans

translator=googletrans.Translator()

read_file_path=r"9. 영어로된 문서를 한글로 자동번역\영어파일_houdini_greyscalegorilla.txt"
write_file_path=r"9. 영어로된 문서를 한글로 자동번역\한글파일.txt" #저장할 경로와 파일명을 지정합니다.

with open(read_file_path, 'r') as f:
  readLines=f.readlines()

for lines in readLines:
  result1=translator.translate(lines, dest='ko')
  print(result1.text)
  with open(write_file_path, 'a', encoding='UTF8') as f: #파일을 저장합니다.'a'옵션은 마지막에 추가로 쓰는 모드입니다. 한글을 사용하기 위해 encoding='UTF8' 옵션을 넣었습니다.
    f.write(result1.text+'\n') #한 줄 쓴 다음 \n을 더하여 줄바꿈을 하였습니다.
