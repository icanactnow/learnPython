# coding:utf8

from  datetime import datetime

from django.db import models

from courses.models import Course
from users.models import UserProfile


# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    mobile = models.CharField(max_length=20, verbose_name=u'手机')
    course_name = models.CharField(max_length=20, verbose_name=u'课程名称')
    add_data = models.DateField(default=datetime.now, verbose_name=u'加入时间')

    class Mate:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class CourseComment(models.Model):
    "课程评论"
    user = models.ForeignKey(UserProfile, verbose_name=u'评论的用户')
    course = models.ForeignKey(Course, verbose_name=u'评论的文章')
    comments = models.CharField( max_length=200,verbose_name=u'评论')
    add_data = models.DateField(default=datetime.now, verbose_name=u'加入时间')

    class Mate:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u'用户')
    fav_id = models.IntegerField(default=0,verbose_name=u'数据id')
    fav_type = models.IntegerField(choices=(('1',u'课程'),('2','课程机构'),('3','讲师')),verbose_name=u'收藏类型')
    add_data = models.DateField(default=datetime.now, verbose_name=u'加入时间')
    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name
class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name=u'用户')
    message = models.CharField(max_length=500,verbose_name=u'用户信息')
    has_read = models.BooleanField(default=False,verbose_name=u'是否读了')
    add_data = models.DateField(default=datetime.now, verbose_name=u'加入时间')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'评论的用户')
    course = models.ForeignKey(Course, verbose_name=u'评论的文章')
    add_data = models.DateField(default=datetime.now, verbose_name=u'加入时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name