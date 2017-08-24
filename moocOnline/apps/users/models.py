# coding:utf8
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# 这里既可以使用默认的字段，又可以加入新的字段
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'姓名', default='')
    birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('male', u'女'), ('female', u'男')), default='female')
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='/image/%y/%m', default=u'image/default.png', max_length=100)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=50, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'忘记密码')), default='register', max_length=100,verbose_name=u'验证码类型')
    send_time = models.DateField(default=datetime.now,verbose_name=u'发送时间')  # 加括号datatime.now()在类编译时候就生成时间，不加在实例化的时候在生成时间。

    class Meta:  # 这个函数是存储类的信息。
        verbose_name = u'邮箱验证'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '{0}---{1}'.format(self.code,self.email)

class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=u'轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:  # 这个函数是存储类的信息。
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
