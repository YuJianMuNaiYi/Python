#SMTP发送邮件
#SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

from email.mime.text import MIMEText
import smtplib
#注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
msg=MIMEText('hello,send by Python ...','plain','utf-8')

#输入Email的地址和口令
from_addr=input('From:')
password=input('Password:')

#输入收件人的地址
to_addr=input('To:')
#输入SMTP服务器地址
smtp_server=input('SMTP server:')
# SMTP协议默认端口是25
server=smtplib.SMTP(smtp_server,25)
#可以打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
server.login(from_addr,password)
#as_string()把MIMEText对象变成str
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
