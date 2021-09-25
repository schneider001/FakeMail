'''
import smtplib

mail_user = 'madhacker228@gmail.com'
mail_password = '54OUQ8Ib9jyYv0F2'

sent_from = 'edu.admin@phystech.edu'
sent_to = ['plaksin.dr@phystech.edu', 'platov.va@phystech.edu']
subject = "Переход на дистанционное обучение!"
body = "Уважаемые студенты, в связи со сложившейся эпидемиологической обстановкой занятия переходят в дистанционный режим!\n\n"\
    "С уважением, администрация МФТИ."


email_text = "\r\n".join((
        "From: %s" % sent_from,
        "To: %s" % sent_to,
        "Subject: %s" % subject,
        "",
        body
    ))


smtp_server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
smtp_server.ehlo()
smtp_server.login(mail_user, mail_password)
smtp_server.sendmail(sent_from, sent_to, email_text)
smtp_server.close()
print ("Email sent successfully!")
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class FakeMail:
    server = 'smtp-relay.sendinblue.com'
    user = 'madhacker228@gmail.com'
    password = '54OUQ8Ib9jyYv0F2'

    def __init__(self, sender, receiver, title, body):
        self.sender = sender
        self.receiver = receiver
        self.title = title
        self.body = body

    def send_mail(self):
        html = '<html><head></head><body><p>' + self.body + '</p></body></html>'

        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.title
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg['Reply-To'] = self.sender
        msg['Return-Path'] = self.sender

        part_text = MIMEText(self.body, 'plain')
        part_html = MIMEText(html, 'html')

        msg.attach(part_text)
        msg.attach(part_html)

        mail = smtplib.SMTP_SSL(self.server)
        mail.login(self.user, self.password)
        print(mail.sendmail(self.sender, self.receiver, msg.as_string()))
        mail.quit()

# server = 'smtp-relay.sendinblue.com'
# user = 'madhacker228@gmail.com'
# password = '54OUQ8Ib9jyYv0F2'
#
# recipients = ['lifantev.da@phystech.edu', 'manchuk.na@phystech.edu', 'tiukin.niu@phystech.edu', 'plaksin.dr@phystech.edu']
# sender = 'edu.admin@phystech.edu'
# subject = 'Переход на дистанционное обучение.'
# text = 'Спешим Вас уведомить, что в связи со сложившейся эпидемиологической обстановкой занятия переходят в удаленный режим с'\
#     'использованием дистанционных технологий на платформе lms.' + '<br><br>' + 'С уважением,' + '<br>' + 'администрация МФТИ.'
# html = '<html><head></head><body><p>' + text + '</p></body></html>'
#
# msg = MIMEMultipart('alternative')
# msg['Subject'] = subject
# msg['From'] = 'Администрация МФТИ <' + sender + '>'
# msg['To'] = ', '.join(recipients)
# msg['Reply-To'] = sender
# msg['Return-Path'] = sender
#
# part_text = MIMEText(text, 'plain')
# part_html = MIMEText(html, 'html')
#
# msg.attach(part_text)
# msg.attach(part_html)
#
# mail = smtplib.SMTP_SSL(server)
# mail.login(user, password)
# mail.sendmail(sender, recipients, msg.as_string())
# mail.quit()
