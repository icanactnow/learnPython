# coding:utf8
from datetime import datetime

from django.db import models
from organization.models import CourseOrg

# Create your models here.
class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name=u'课程所属机构',null=True,blank=True)#这样做是保证没该字段之前添加的数据允许为空
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(max_length=50,choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')))
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(upload_to='image/%Y/%m', verbose_name=u'封面图片', max_length=200)
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name
    def course_lesson_num(self):
        count = self.lesson_set.all().count()#通过反取取到拥有下级的数量
        return count
    def course_students(self):
        return self.usercourse_set.all()[:3]
    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'章节所属课程')
    name = models.CharField(max_length=50, verbose_name=u'章节名称')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name
    # def __str__(self):
    #     return {0}{1}.__format__(self.name,self.course)
    def __unicode__(self):
        return '{0}({1})'.format(self.name,self.course)
class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u'视频所属课程')
    name = models.CharField(max_length=50, verbose_name=u'视频名称')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name
class CourseRescoure(models.Model):
    course  = models.ForeignKey(Course,verbose_name=u'资源所属课程')
    download = models.FileField(upload_to='course/rescoure/%Y/%m',verbose_name=u'下载文件')
    name = models.CharField(max_length=50, verbose_name=u'资源名称')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'资源'
        verbose_name_plural = verbose_name
