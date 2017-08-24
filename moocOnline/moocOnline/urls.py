from django.conf.urls import include, url
from django.contrib import admin
import xadmin
from django.views.generic import TemplateView

from  users.views import LoginView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    url(r'^login/$',LoginView.as_view(),name='login'),
]
