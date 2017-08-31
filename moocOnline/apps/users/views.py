# coding:utf8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render

from users.models import UserProfile
from .forms import LoginForm, RegisterForm,ForgetPwdForm,ModifyForm


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
from utils.email_send import send_register_email
from .models import EmailVerifyRecord,UserProfile

class ActiveUserView(View):
    def get(self,request,active_code):#注意这里的active_code要和路由里面的一致
        all_recodes = EmailVerifyRecord.objects.filter(code=active_code)
        if all_recodes:#如果存在则验证成功
            for recode in all_recodes:
                email = recode.email
                user = UserProfile.objects.get(email= email)
                user.is_active = True
                user.save()
        else:#激活失败
            return render(request,'register_failed.html')
        return  render(request, 'login.html')


class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():  # 如果验证通过
            # 保存用户及密码
            # 获取邮箱账号，以及将密码加密
            user_name = request.POST.get('email', '')
            #判断用户是否已经注册过
            if UserProfile.objects.filter(email=user_name):
                return   render(request, 'login.html', {'msg': '该邮箱已注册过'})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.email = user_name
            user_profile.username = user_name
            user_profile.password = make_password(pass_word)  # 对密码进行加密保存，因为django 只存密文
            user_profile.is_active = False # 默认是True在没验证之前进行关闭。
            user_profile.save()
            # 发送邮件
            send_register_email(user_name,'register')
            return render(request,'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})
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
                if user.is_active:
                    login(request, user)  # 这个函数做了登录也处理了session的自动登录机制
                    return render(request, 'index.html', {'loginform': loginform})
                else:
                    register_form = RegisterForm()
                    return render(request, 'register.html',{'register_form':register_form})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误!'})
        else:
            return render(request, 'login.html', {'loginform': loginform})  # 如果输入格式不对，返回提示信息。
class ForgetPwdView(View):
    def get(self,request):
        forgetpwd_form = ForgetPwdForm()
        return render(request,'forgetpwd.html',{'forgetpwd_form':forgetpwd_form})
    def post(self,request):
        forgetpwd_form = ForgetPwdForm(request.POST)
        if forgetpwd_form.is_valid():
            #发送验证码
            email = request.POST.get('email','')
            if not UserProfile.objects.filter(email=email):
                return   render(request, 'register.html', {'msg': '该用户不存在，请先注册'})
            send_register_email(email, 'forget')
            return render(request, 'send_successed.html')
        else:
            return render(request, 'forgetpwd.html', {'forgetpwd_form': forgetpwd_form})
class RestPwdView(View):
    def get(self,request,reset_code):
        all_recodes = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_recodes:  # 如果存在则验证成功
            for recode in all_recodes:
                email = recode.email
                user = UserProfile.objects.get(email=email)
                return render(request, 'password_reset.html',{'email':email})
        else:  # 验证失败
            return render(request, 'register_failed.html')
    # def post(self,request):
    #     pass
class ModifyPwdView(View):#由于上面的路径设置必须要
    def post(self,request):
        modify_form  = ModifyForm(request.POST)
        if modify_form.is_valid():
            if request.POST.get('password1','') != request.POST.get('password2',''):
                return render(request,'password_reset.html',{'msg':'两次输入密码不一致'})
            email  = request.POST.get('email','')
            users = UserProfile.objects.filter(email=email)
            for user in users:
                user.password= make_password(request.POST.get('password1',''))
                user.save()
            return render(request,'index.html')
        else:
            return render(request, 'login.html')
class LogoutView(View):
        def get(self,request):
            users = UserProfile.objects.filter(username=request.user.username)
            for user in users:
                logout(request)
            return render(request,'index.html')