#coding:utf8
from django.contrib import admin

# Register your models here.
from .models import UserProfile #.表示文件所在当前目录
# 定义管理器
# class UserProfileAdmin(admin.ModelAdmin):
#     pass
# # 将UserProfile表与后台进行关联注册
# admin.site.register(UserProfile,UserProfileAdmin)#（模型，管理器）