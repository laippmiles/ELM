#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from passWord import decode
from email.mime.application import MIMEApplication
from email.utils import formataddr


def send_email_from_lzy(subject, content, filePath, fileName):
    import smtplib
    import os
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email import encoders
    msg = email.mime.multipart.MIMEMultipart()
    user = decode(113,'E9C8@8F:A9<889;8<8@99;?9F9A8D989@9E9G=:9F9D9')
    pwd = decode(113,'88@8B9=8G988A9C9:9@9D9C9=989@9;9')
    to = decode(422,'?Q<Q;Q;Q?Q;Q?QGQ?Q>V?U?U@P=TATCT')

    msg['From'] = formataddr(["李泽言", user])
    msg['to'] = to
    msg['Subject'] = subject
    content1 = MIMEText(content, 'plain', 'utf-8')
    msg.attach(content1)
    annexPath = filePath + fileName
    part = MIMEApplication(open(annexPath,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename= fileName)
    msg.attach(part)
    # -----------------------------------------------------------
    smtpHost = decode(422, '=UCT:U>U@P?U?U@P=TATCT')
    s = smtplib.SMTP_SSL(smtpHost,465)
    s.login(user, pwd)
    s.sendmail(user, to, msg.as_string())
    print('发送成功')
    s.close()

#!/usr/bin/python
# -*- coding: UTF-8 -*-

def send_email(subject, content, filePath, fileName):
    msg = email.mime.multipart.MIMEMultipart()

    smtpHost = decode(422, '=UCT:U>U@P?U?U@P=TATCT')
    sendAddr = decode(422,'?Q<Q;Q;Q?Q;Q?QGQ?Q>V?U?U@P=TATCT')
    recipientAddrs = sendAddr
    password = decode(422, ';U=T=TAT?T?U=U:T=TDU?UAT<T9T9T=T')
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

def mailFromLZY(subject, content, filePath, fileName):
    try:
        print('当前文件地址：',filePath, fileName)
        send_email_from_lzy(subject, content, filePath, fileName)
    except Exception as err:
        print(err)