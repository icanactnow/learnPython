# coding:utf8
from datetime import datetime

from django.db import models


# Create your models here.
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市名称')
    desc = models.CharField(max_length=300, verbose_name=u'描述')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'组织名称')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数量')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数量')
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name=u'封面图片', max_length=200)
    address = models.CharField(max_length=150, verbose_name=u'机构详细地址')
    city = models.ForeignKey(CityDict, verbose_name=u'机构所在城市')
    desc = models.CharField(max_length=300, verbose_name=u'描述')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')
    category = models.CharField(max_length=20, default='pxjg', choices=(('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人'),),
                                verbose_name='机构类别')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    course_nums = models.IntegerField(default=0, verbose_name='课程数量')

    class Meta:
        verbose_name = u'机构表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u'教师所属机构')
    name = models.CharField(max_length=20, verbose_name=u'教师名称')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数量')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数量')
    points = models.CharField(max_length=50, verbose_name=u'教学特点')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')
    work_year = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'职位')
    image = models.ImageField(upload_to='teacher/%Y/%m', verbose_name=u'教师照片', max_length=200,null=True,blank=True)
    class Meta:
        verbose_name = u'教师表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
