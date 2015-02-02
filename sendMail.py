from email.mime.text import MIMEText
import smtplib

msg = MIMEText('hello,send by python...','plain','utf-8')

from_addr = 'ahhswangkai@163.com'
password = 'w19890922k'
smtp_server = 'smtp.163.com'

to_addr = '474799246@qq.com'
server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()