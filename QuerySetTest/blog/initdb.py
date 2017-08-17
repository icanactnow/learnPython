# coding:utf8
import os
import random

# from django.template.backends import django
import django

os.environ.update({"DJANGO_SETTINGS_MODULE": "QuerySetTest.settings"})
django.setup()
from blog.models import Author, Tag, Article

author_name_list = ['WeizhongTu', 'twz915', 'dachui', 'zhe', 'zhen']
article_title_list = ['Django 教程', 'Python 教程', 'HTML 教程']


def create_authors():
    for author_name in author_name_list:
        author, created = Author.objects.get_or_create(name=author_name)
        # 生成9位qq
        author.qq = ''.join(
            str(random.choice(range(10))) for _ in range(9)
        )
        author.addr = 'addr_%s' % random.randrange(1, 3)
        author.email = '%s@eric.com' % author.addr
        author.save()


def create_articles_and_tags():
    for article_title in article_title_list:
        tag_name = article_title.split(' ', 1)[0]
        tag, created = Tag.objects.get_or_create(name=tag_name)
        # 给文章选个作者
        random_author = random.choice(Author.objects.all())
        for i in range(1, 21):
            title = '%s_%s' % (article_title, i)

            # 以为文章包含很多其他字段，所以先将其他创建后在创建文章对象
            article, created = Article.objects.get_or_create(title=title, defaults={
                'Author': random_author,
                'content': '%s 正文' % title,
                'score': random.randrange(95, 100),
            })
            article.tags.add(tag)  # 增加多对对属性


def main():
    create_authors()
    create_articles_and_tags()


if __name__ == '__main__':
    main()
    print('done')
