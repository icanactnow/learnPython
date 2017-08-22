#coding:utf8
#从blog.txt中批量导入数据
import django
import os

from django.core.management.commands import loaddata

os.environ.update({"DJANGO_SETTINGS_MODULE": "DataImport.settings"})#注意输入对象的项目名称，非应用名称
if django.VERSION >= (1,7):
    django.setup()
from blog.models import Blogs
# def main ():
#     file = open('blogs')
#     for line in file:
#         title ,content = line.split('****')
#         Blogs.objects.get_or_create(title=title,content=content)#这样写会避免重复，但效率会慢些
#     file.close()
# def main():
#     file = open('blogs')
#     blogList=[]
#     for line in file:
#         title ,content = line.split('****')
#         blog = Blogs(title=title,content=content)#创建Blogs对象
#         blogList.append(blog)
#     file.close()
#     Blogs.objects.bulk_create(blogList)
def main():
    os.system('python3 manage.py loaddata blog_dump.json')
if __name__ == '__main__':
    main()
    print('done')
    print(Blogs.objects.count())