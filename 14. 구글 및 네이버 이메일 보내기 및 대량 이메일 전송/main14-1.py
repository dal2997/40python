import smtplib #1~2:메일을 사용하기 위한 라이브러리를 불러옵니다.
from email.mime.text import MIMEText

send_email="네이버아이디@naver.com"#4:자신의 네이버 아이디를 입력합니다.
send_pwd="네이버비밀번호"#5:자신의 네이버 비밀번호를 입력합니다.

recv_email="받는이메일 주소@hanmail.net"#7:받는 이메일 주소를 입력합니다.

smtp_name="smtp.naver.com"#9-10:네이버 메일의 smtp주소와 포트번호입니다.
smtp_port=587

text=""" 보내는 내용을 입력합니다.
메일 내용을 여기서 적습니다.
여러 줄을 입력하여도 됩니다.
"""
msg=MIMEText(text) #메시지 형식을 문자 형식으로 지정합니다.

msg['Subject']="메일제목은 여기에 넣습니다." #메일제목을 입력합니다.
msg['From']=send_email
msg['To']=recv_email
print(msg.as_string())

s=smtplib.SMTP(smtp_name,smtp_port)#23~27:이메일을 보냅니다.
s.starttls()
s.login(send_email,send_pwd)
s.sendmail(send_email,recv_email,msg.as_string())
s.quit()