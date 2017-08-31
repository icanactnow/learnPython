# coding:utf8
import xadmin
from .models import Course, Lesson, Video, CourseRescoure

__author__ = 'eric'
__date__ = '2017/8/23 16:51'


# 注册邮箱验证这个model


class CourseAdmin(object):  # 注意这个继承

    list_display = ['name', 'desc', 'detail', 'degree', 'fav_nums', 'learn_times', 'students', 'image', 'click_nums',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'fav_nums', 'learn_times', 'students', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'fav_nums', 'learn_times', 'students', 'image', 'click_nums',
                   'add_time']


class LessonAdmin(object):
    list_display = ['name', 'course', 'add_time']
    search_fields = ['name', 'course']
    list_filter = ['name', 'course', 'add_time']


class VideoAdmin(object):
    list_display = ['name', 'lesson', 'add_time']
    search_fields = ['name', 'lesson']
    list_filter = ['name', 'lesson', 'add_time']


class CourseRescoureAdmin(object):
    list_display = ['name', 'course', 'download', 'add_time']
    search_fields = ['name', 'course', 'download']
    list_filter = ['name', 'course', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseRescoure, CourseRescoureAdmin)
