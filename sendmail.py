import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(receiver, sender, subject , content,  dir_path, filename):
    # dir_path = "G:/test_runners/selenium_regression_test_5_1_1/TestReport"
    # files = ["SeleniumTestReport_part1.html", "SeleniumTestReport_part2.html", "SeleniumTestReport_part3.html"]

    msg = MIMEMultipart()
    msg['To'] = receiver
    msg['From'] = sender
    msg['Subject'] = subject

    body = MIMEText(content, 'html', 'utf-8')
    msg.attach(body)  # add message body (text or html)


    file_path = os.path.join(dir_path, filename)
    print(file_path);
    attachment = MIMEApplication(open(file_path, "rb").read())
    attachment.add_header('Content-Disposition','attachment', filename=filename)
    msg.attach(attachment)

    s = smtplib.SMTP()
    s.connect(host=localhost)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    # print 'done!'
    s.close()


path =  r'\\192.168.100.100\sigmachain_share\public\10_Project\Piki\release\v1.0.55'

send_email( "namgt@sigmachain.net",
           "namgt@sigmachain.net",
           "메일제목",
           "메일내용",
           path,
           "piki_v1.0.55.apk"
           )


# send_mail 함수에 구현하겠습니다.
def send_mail():
    # 메일 내용을 담을 문자열을 선언합니다.
    text = 'test message'

    # smtp 인스턴스를 만들어줍니다.
    # 인자값으로는 smtp 서버 url과 port가 들어갑니다.
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # 초기에 서버와 handshaking 을 시도합니다.
    smtp.ehlo()
    # TLS를 이용해서 암호화할 것이므로 start tls 함수를 호출합니다.
    smtp.starttls()

    # smtp 서버 로그인을 위해 id 와 password를 인자로 하여 login 함수를 호출합니다.
    # id는 @가 들어간 email형식으로 입력합니다.
    smtp.login('id' 'password')

    # MIMEText 인스턴스에는 보내려는 메일 내용을 인자값으로 넣어줍니다.
    message = MIMEText(text)
    # 메일 제목은 Subject, 보내는 사람은 From, 받을 사람 정보는 To로 설정합니다.
    message['Subject'] = 'mail subject'
    message['From'] = 'from email address'
    message['To'] = 'to email address'

    # smtp sendmail 함수를 이용하여 실제로 메일을 발송해줍니다.
    smtp.sendmail('from email address', 'to email address', message.as_string())

    # smtp quit 함수로 인스턴스를 종료시킵니다.
    smtp.quit()