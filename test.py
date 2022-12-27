import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

recipients = ["dhalsdl12@gmail.com", "dhalsdl12@naver.com"]

message = MIMEMultipart()
message['Subject'] = '메일 전송 테스트'
message['From'] = "dhalsdl12@naver.com"
message['To'] = ",".join(recipients)

content = """
    <html>
    <body>
        <h2>{title}</h2>
        <p>메일 전송 테스트입니다</p>
    </body>
    </html>
""".format(title='메일.. 받으셨나요..?')

mimetext = MIMEText(content, 'html')
message.attach(mimetext)

email_id = 'dhalsdl12@naver.com'
email_pw = 'kom142536*'

server = smtplib.SMTP('smtp.naver.com', 465)
server.ehlo()
server.starttls()
server.login(email_id, email_pw)
server.sendmail(message['From'], recipients, message.as_string())
server.quit()
