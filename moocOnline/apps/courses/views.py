#coding:utf8
from pure_pagination import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import View
from .models import Course



class CoursesView(View):
    def get(self,request):
        #获取当前页数，如果为分页则设置页数

        all_courses = Course.objects.all()
        sort_courses = all_courses.order_by('-click_nums')[:2]
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 6, request=request)
        courses = p.page(page)
        course_count = all_courses.count()
        return render(request,'course-list.html',locals())

class DetailView(View):
    def get(self,request,course_name):
        course = Course.objects.get(name=course_name)
        return render(request,'course-detail.html',locals())


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
            from operation.models import UserFavorite
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
