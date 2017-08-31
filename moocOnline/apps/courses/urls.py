#coding:utf8
__author__ = 'eric'
__date__ = '2017/8/30 22:43'
from django.conf.urls  import url
from .views import CoursesView,DetailView,AddFavView
urlpatterns = [

    url(r'^list/',CoursesView.as_view(),name='course_list' ),
    url(r'^detail/(?P<course_name>.*)/$',DetailView.as_view(),name='course_detail' ),
    url(r'^add_fav/',AddFavView.as_view(),name='add_fav' ),

]