# coding:utf8
import xadmin

__author__ = 'eric'
__date__ = '2017/8/23 16:51'

# 注册邮箱验证这个model
from .models import EmailVerifyRecord, Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True# 开启主题
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '智创无限管理后台'
    site_footer = '智创无限有限责任公司'
    menu_style = 'accordion'#菜单折叠
# 编写邮箱验证管理器
class EmailVerifyRecordAdmin(object):  # 注意这个继承
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
