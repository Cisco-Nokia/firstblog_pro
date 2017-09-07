#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..models import Category, Tag, Article, Link
from adshow.models import Ad

from django import template
from django.db .models import Count

from django.utils.html import format_html

"""
这个自定义的模板标签，用于取出那些固定不变的值，渲染到模板文件中
在这个博客中，主要是导航栏上的分类，右侧的各种分类
"""

register = template.Library()


# 取出所有的category，用于导航栏渲染
@register.simple_tag
def get_categories():
    return Category.objects.all()


# 取出所有的tag，用于tag栏目的渲染
@register.simple_tag
def get_tags():
    return Tag.objects.all()


# 按照时间归档的文章摘取，相当于帮我们对所有文章的发布年月去重了，
# 返回QuerySet，其计算结果为datetime.date对象列表，表示特定种类的所有可用日期QuerySet。
# 参考：https://docs.djangoproject.com/en/1.11/ref/models/querysets/
@register.simple_tag
def get_archives():
    return Article.objects.dates('date_publish', 'month', order='DESC')


# 算出每个按照时间归档的文章数量，这里context是上下文，而date其实是通过上面的get_archive对模板进行渲染后得到的
# 请参考：https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#simple-tags
@register.simple_tag(takes_context=True)
def get_archive_count(context):
    date = context['date']
    return Article.objects.filter(date_publish__year=date.year, date_publish__month=date.month).count()


# 取出博主推荐文章，数量为5
@register.simple_tag
def get_recommend():
    return Article.objects.all().order_by('recommend_index')[:5]


# 取出点击最多的文章，数量为5，后面没用上
@register.simple_tag
def get_click_count():
    return Article.objects.all().order_by('-click_count')[:5]


# 取出评论数量最多的文章，数量为5
@register.simple_tag
def get_comment_count():
    article_list = Article.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:5]
    return article_list


# 取出点赞数最多的文章，数量为5
@register.simple_tag
def get_awesome_count():
    return Article.objects.all().order_by('-awesome_count')[:5]


# 取出所有标签tag
@register.simple_tag
def get_tags():
    return Tag.objects.all()


# 取出友情链接
@register.simple_tag
def get_links():
    return Link.objects.all()


# 取出广告数据，数量为4
@register.simple_tag
def get_ad():
    return Ad.objects.all()[:4]


# 自定义分页最多显示5页，功能未完成
# @register.simple_tag(takes_context=True)
# def circle_page(context, current_page, loop_page):
#     if context['article_list'].paginator.num_pages <= 5:
#         if current_page == loop_page:
#             page_element = '<li class="active"><a href="?page=%s">%s</a></li>' % (loop_page, loop_page)
#         else:
#             page_element = '<li><a href="?page=%s">%s</a></li>' % (loop_page, loop_page)
#         return format_html(page_element)
#     else:
#         if loop_page == 1 or loop_page == 2:
#             page_element = '<li class="active"><a href="?page=1">1</a></li>' \
#                            '<li><a href="?page=2">2</a></li>' \
#                            '<li><a href="?page=3">3</a></li>' \
#                            '<li><a href="?page=4">4</a></li>' \
#                            '<li><a href="?page=5">5</a></li>'
#             return format_html(page_element)
#         else:
#             offset = abs(current_page - loop_page)
#             if offset < 3:
#                 if current_page == loop_page:
#                     page_element = '<li class="active"><a href="?page=%s">%s</a></li>' % (loop_page,loop_page)
#                 else:
#                     page_element = '<li><a href="?page=%s">%s</a></li>' % (loop_page, loop_page)
#                 return format_html(page_element)
#             else:
#                 return ''
