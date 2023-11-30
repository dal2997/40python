#qr코드 생성 코드 만들고 실행
import qrcode

qr_data='www.naver.com'
qr_img=qrcode.make(qr_data)

save_path='4. QR코드 생성기\\'+qr_data+'.png'
qr_img.save(save_path)