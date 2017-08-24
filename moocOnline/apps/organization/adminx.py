# coding:utf8
import xadmin
from organization.models import CityDict, CourseOrg, Teacher

__author__ = 'eric'
__date__ = '2017/8/23 16:51'


# 注册邮箱验证这个model


# 编写邮箱验证管理器
class CityDictAdmin(object):  # 注意这个继承

    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):

    list_display = ['name', 'desc', 'add_time','click_nums','image','city','address','fav_nums']
    search_fields = ['name', 'desc', 'add_time','click_nums','image','city']
    list_filter = ['name', 'desc', 'add_time','click_nums','image','city','address','fav_nums']


class TeacherAdmin(object):

    list_display = ['name', 'org','click_nums','points','city','work_year','work_company','work_position', 'add_time']
    search_fields =['name', 'org','click_nums','points','city','work_year','work_company','work_position']
    list_filter =['name', 'org','click_nums','points','city','work_year','work_company','work_position', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)