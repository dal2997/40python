import qrcode

file_path= r'4. QR코드 생성기\\qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
  read_lines = f.readlines()

  for line in read_lines:
    line=line.strip()
    print(line)

    qr_data=line
    qr_img=qrcode.make(qr_data)

    save_path='4. QR코드 생성기\\'+qr_data+'.png'

    qr_img.save(save_path)


#     Exception has occurred: FileNotFoundError
# [Errno 2] No such file or directory: '4. QR코드 생성기\\github.com/dal2997/40python.png'
#   File "D:\코딩공부\파이썬과 40개의 작품들\4. QR코드 생성기\main4-3.py", line 16, in <module>
#     qr_img.save(save_path)
# FileNotFoundError: [Errno 2] No such file or directory: '4. QR코드 생성기\\github.com/dal2997/40python.png'