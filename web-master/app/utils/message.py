#__author__:Administrator
#date:2016/12/22

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


# 邮箱验证模块
def email(email_list, content, subject="用户注册"):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr(["王厚亮",'wanghl208@126.com'])
    msg['Subject'] = subject
    # SMTP服务

    server = smtplib.SMTP("smtp.126.com", 25)
    server.login("邮箱名", "密码") # 输入服务端邮箱和验证码
    # server.login("hujq1029@163.com", "wshujq1029")
    server.sendmail("wanghl208@126.com", email_list, msg.as_string())
    server.quit()
#
# email(['1227268086@qq.com'],'nihao')
