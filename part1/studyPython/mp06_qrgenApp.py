# QR 코드 생성 앱
import qrcode

qr_data = 'https://www.python.org'
qr_img = qrcode.make(qr_data)

qr_img.save('./studyPython/site.png')

#qrcode.run_example(data='https://www.naver.com')