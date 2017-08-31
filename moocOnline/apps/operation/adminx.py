# coding:utf8
import xadmin
from .models import UserCourse

__author__ = 'eric'
__date__ = '2017/8/23 16:51'


# 注册邮箱验证这个model


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_data']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_data']

xadmin.site.register(UserCourse, UserCourseAdmin)
