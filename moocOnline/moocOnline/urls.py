#coding:utf8
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.views.static import serve
from moocOnline.settings import MEDIA_ROOT
import xadmin
from  users.views import LoginView, RegisterView,ActiveUserView,ForgetPwdView,RestPwdView,ModifyPwdView,LogoutView
from  organization.views import OrgView
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),#邮箱验证匹配后面的验证码
    url(r'^reset/(?P<reset_code>.*)/$', RestPwdView.as_view(), name='reset_pwd'),
    url(r'^modify/$', ModifyPwdView.as_view(), name='modify_pwd'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^logout/$',LogoutView.as_view(),name='logout' ),
    url(r'^org/',include('organization.urls',namespace='org') ),#在这路配置路由分配的地址以及命名空间
    url(r'^course/',include('courses.urls',namespace='course') ),#在这路配置路由分配的地址以及命名空间
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

]
