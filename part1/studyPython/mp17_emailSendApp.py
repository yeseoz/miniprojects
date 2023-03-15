# 이메일 보내기 앱
import smtplib # 메일전송프로토콜
from email.mime.text import MIMEText

# MIME : ASCII가 아닌 문자 인코딩을 이용해 영어가 아닌 다른 언어로 된 전자 우편을 보낼 수 있는 방식을 정의 (사진, 파일...)

send_email = 'kys021697@naver.com'
send_pass = 'a1b2c3!@#'

recv_email = 'w12345678992@gmail.com'

smtp_name = 'smtp.naver.com'
smtp_port = 587 # port번호 고속도로 같은것?

text = '''메일 내용입니다. 긴급입니다.
조심하세요 빨리 연락주세요..!'''

msg = MIMEText(text)
msg['Subject'] = '메일 제목입니다' # InCoding
msg['From'] = send_email # 보내는 메일
msg['To'] = recv_email # 받는 메일
print(msg.as_string()) # 다 변환되서 나옴

mail = smtplib.SMTP(smtp_name, smtp_port) # SMTP 객체 생성
mail.starttls() # TLS : Transport Layer Security 전송계층 보안 시작
mail.login(send_email, send_pass)
mail.sendmail(send_email, recv_email, msg.as_string())
mail.quit()
print('전송 완료')
