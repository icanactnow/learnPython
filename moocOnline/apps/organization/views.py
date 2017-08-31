# coding:utf8
# import paginator as paginator
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
# coding:utf8
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger

from forms import UserAskForm
from operation.models import UserFavorite
from .models import CourseOrg, CityDict


class OrgView(View):
    def get(self, request):
        # 取出所有课程
        all_orgs = CourseOrg.objects.all()
        # 取出所有城市
        all_citys = CityDict.objects.all()

        # 对当前城市进行筛选
        city_id = request.GET.get('city', '0')  # 从GET中获得当前city_id
        ct = request.GET.get('ct', '0')
        if city_id == '0' and ct != '0':
            all_orgs = CourseOrg.objects.filter(category=ct)
        elif ct == '0' and city_id != '0':
            all_orgs = CourseOrg.objects.filter(city_id=int(city_id))  # city属于courseorg的外键，只要是外键基本可以使用name_id的方式获取，
        elif ct == '0' and city_id == '0':
            all_orgs = CourseOrg.objects.all()
        else:
            all_orgs = CourseOrg.objects.filter(city_id=int(city_id), category=ct)

        hot_orgs = CourseOrg.objects.all().order_by("-click_nums")[:5]
        # 对课程进行分页
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'cs':
                all_orgs = all_orgs.order_by('-course_nums')
            if sort == 'rs':
                all_orgs = all_orgs.order_by('-students')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)
        course_count = all_orgs.count()
        return render(request, 'org_list.html', locals())


class AddUserAskView(View):
    """
    用户添加咨询
    """

    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)  # 这样就保存到了数据库，和之前比不用先实例化在保存。
            return HttpResponse('{"status":"success"}', content_type='application/json')  # 告诉浏览器数据为json
        else:
            return HttpResponse('{"status":"fail","msg":"填写信息有误"}', content_type='application/json')


class OrgHomeView(View):
    """
    机构首页
    """

    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user_id=request.user.id,fav_type=2,fav_id=course_org.id):
                #如果之前收藏过
                has_fav = True
        # 下面是通过机构反取机构的所有课程以及老师，也可以通过机构的属性来从课程和老师的model中进行过滤，不过比较麻烦
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        current_page = 'home'
        return render(request, 'org-detail-homepage.html', locals())


class OrgCourseView(View):
    """
    课程详情页
    """

    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user_id=request.user.id,fav_type=2,fav_id=course_org.id):
                #如果之前收藏过
                has_fav = True
        # 下面是通过机构反取机构的所有课程以及老师，也可以通过机构的属性来从课程和老师的model中进行过滤，不过比较麻烦
        all_courses = course_org.course_set.all()
        current_page = 'course'
        return render(request, 'org-detail-course.html', locals())


class OrgDescView(View):
    """
    机构详情页
    """

    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user_id=request.user.id,fav_type=2,fav_id=course_org.id):
                #如果之前收藏过
                has_fav = True
        current_page = 'desc'
        return render(request, 'org-detail-desc.html', locals())


class OrgTeacherView(View):
    """
    机构首页
    """

    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user_id=request.user.id,fav_type=2,fav_id=course_org.id):
                #如果之前收藏过
                has_fav = True
        # 下面是通过机构反取机构的所有课程以及老师，也可以通过机构的属性来从课程和老师的model中进行过滤，不过比较麻烦
        all_teachers = course_org.teacher_set.all()
        current_page = 'teacher'
        return render(request, 'org-detail-teachers.html', locals())


class AddFavView(View):
    """
    用户收藏以及取消收藏
    """

    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)
        user_id = request.user.id
        # 首先判断用户是否登录
        if not request.user.is_authenticated:
            # 如果没有登录则返回没有登录信息
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')
        else:
            # 如果用户登录了则判断之前有没有收藏过，如果重复收藏即意味着要取消收藏
            user_fav = UserFavorite.objects.filter(user_id=user_id, fav_id=int(fav_id), fav_type=int(fav_type))
            if user_fav:  # 如果之前收藏过则取消收藏
                user_fav.delete()
                # 返回取消收藏相关信息
                return HttpResponse('{"status":"fail","msg":"已取消收藏"}', content_type='application/json')
            else:  # 用户之前为收藏过，则进行收藏
                # 创建对象，实例化，保存极为收藏
                if int(fav_id) > 0 and int(fav_type) > 0:
                    userFav = UserFavorite()
                    userFav.fav_type = fav_type
                    userFav.fav_id = fav_id
                    userFav.user_id = user_id
                    userFav.save()
                    return HttpResponse('{"status":"success","msg":"收藏成功"}', content_type='application/json')
                else:
                    return HttpResponse('{"status":"fail","msg":"收藏失败"}', content_type='application/json')
