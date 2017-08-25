# coding:utf8
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

from users.models import UserProfile
from .forms import LoginForm, RegisterForm


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 并级查询
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):  # 检查密码函数
                return user
        except Exception as  e:
            return None


# 基于类的书写
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():#如果验证通过
            #保存用户及密码
            #获取邮箱账号，以及将密码加密
            user_name = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.email = user_name
            user_profile.username = user_name
            user_profile.password = make_password(pass_word)# 对密码进行加密保存，因为django 只存密文
            user_profile.save()
        else:
            return render(request,'register.html',{'register':register_form})
        return render(request, 'register.html')

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        # 实例化一个form验证
        loginform = LoginForm(request.POST)  # 这里需要一个字典参数，request.POST刚好返回一个字典
        if loginform.is_valid():  # 判断是否合法
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            # 通过authemticate方法验证用户提交的数据是否正确
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)  # 这个函数做了登录也处理了session的自动登录机制
                return render(request, 'index.html', locals())
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误!'})
        else:
            return render(request, 'login.html', {'loginform': loginform})  # 如果输入格式不对，返回提示信息。
