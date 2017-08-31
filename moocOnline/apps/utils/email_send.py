# coding:utf8
import random

from django.core.mail import send_mail  # Django发送邮件库

from moocOnline.settings import EMAIL_FROM
from users.models import EmailVerifyRecord

__author__ = 'eric'
__date__ = '2017/8/25 16:56'


# 随机长度字符
def random_str(randomLength=8):
    str = ''
    randomChar = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    for i in range(randomLength):
        str += randomChar[random.Random().randint(0, len(randomChar) - 1)]
    return str


def send_register_email(email, send_type='register'):
    # 首先将信息保存到数据库，以便验证
    email_recode = EmailVerifyRecord()
    email_recode.email = email
    code = random_str(10)
    email_recode.code = code
    email_recode.send_type = send_type
    email_recode.save()

    # 发送验证码
    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title='智创无限激活'
        email_body='点击链接进行激活(爱点不点):http://127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    if send_type == 'forget':
        email_title='智创无限找回密码'
        email_body='点击链接进行激活(爱点不点):http://127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
