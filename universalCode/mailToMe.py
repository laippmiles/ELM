#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from passWord import decrypt
from email.mime.application import MIMEApplication

def send_email(subject, content, filePath, fileName):
    msg = email.mime.multipart.MIMEMultipart()

    smtpHost = decrypt(422, 'F^L]C^G^IYH^H^IYF]J]L]')
    sendAddr = decrypt(422, 'HZEZDZDZHZDZHZPZHZG_H^H^IYF]J]L]')
    recipientAddrs = sendAddr
    password = decrypt(422, 'K]P^L]E]O^D^E]E^P^P]B^H^E]O]E]E]')
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)

    # 添加附件，传送path的文件
    annexPath = filePath + fileName
    part = MIMEApplication(open(annexPath,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename= fileName)
    msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect(smtpHost, '25')
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("发送成功！")
    smtp.quit()


def mailToMe(subject, content, filePath, fileName):
    try:
        send_email(subject, content, filePath, fileName)
    except Exception as err:
        print(err)
