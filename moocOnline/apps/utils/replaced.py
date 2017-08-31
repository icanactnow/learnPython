#coding:utf8
__author__ = 'eric'
__date__ = '2017/8/30 10:21'
import re

with open("../../templates/course-list.html", "r" ) as f:
    lines = f.readlines()

with open("course-list.html", "w") as f_w:
    for line in lines:
        if re.search(r'"../(.*?)"', line):
            replaceStr = re.search(r'"../(.*?)"', line).groups()[0]  # 要插入的字符串
            a = re.sub(r'"../.*"', '" {%  static \'' + r'{0}'.format(replaceStr) + '\' %} " ', line)
            f_w.write(a)
            continue
        f_w.write(line)