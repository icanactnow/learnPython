# coding:utf8
from django.conf.urls import include, url
from django.contrib import admin

# from views import *
# import blog
import blog
from blog import views

urlpatterns = [
    # Examples:
    url(r'^blog/', blog.views.hello),
    url(r'^admin/', include(admin.site.urls)),#进入后台管理
    url(r'^index/', blog.views.index),
    url(r'^index/(\d+)', blog.views.article),
    url(r'^go/', blog.views.go),
]
