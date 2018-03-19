#__author__:Administrator
#date:2016/12/20

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import random


class Send_email:

    '''
      第二种邮箱验证的方法
        本次函数没有用到
    '''
    def __init__(self,mail_host="smtp.qq.com",
                 mail_user="1227268086@qq.com  # 这里填的是你的发件箱的邮箱名",
                 mail_pass="这里填的不是邮箱密码，而是开启服务后的16位授权码"):
        self.mail_host=mail_host
        self.mail_user=mail_user
        self.mail_pass=mail_pass

    def send_mail(self,email):
        random_str="".join([str(random.randint(0,9)) for i in range(6)])  # 生成6位的0-9的随机数字，并转换成字符串
        mailInfo = {
                "from":self.mail_user,          #"发信人用户名@qq.com",
                "to": email,                    #"收信人用户名@qq.com",
                "hostname":"smtp.qq.com",
                "username":self.mail_user,     #"账户名",
                "password":self.mail_pass,     #"密码",
                "mailsubject":"注册验证码",   #"邮件标题",
                "mailtext":random_str,
                "mailencoding":"utf-8"
                        }

        msg=MIMEText(mailInfo["mailtext"])  # 里面放需要发送的内容  #,"text",mailInfo["mailencoding"]  # 这些加上无法收到验证码
        msg['Subject']=Header(mailInfo["mailsubject"],mailInfo["mailencoding"])  # 邮件标题内容
        msg["from"] = mailInfo["from"]  # 发件人
        msg["to"] = mailInfo["to"]  # 收件人
        # server = smtplib.SMTP(self.mail_host, 25) # 这一行是以前的QQ邮箱可以直接使用smtp发送邮件
        server = SMTP_SSL(mailInfo["hostname"])  # 现在的QQ邮箱必须要SSL支持才能发送邮箱，并且不能填邮箱密码，需要在邮箱设置中打开支持POP3/SMTP功能，并获取到16位的授权码
        server.set_debuglevel(1)  # 设置debug等级 如果不想看详细日志，可以把日志级别调高一点
        server.ehlo(mailInfo["hostname"])  # 设置smtp邮箱服务器地址
        server.login(self.mail_user, self.mail_pass)  # 通过用户名和设置的授权码登录
        server.sendmail(mailInfo["from"], mailInfo["to"], msg.as_string())  # 将打包的信息发送给对方
        server.quit()  # 退出发送邮件

