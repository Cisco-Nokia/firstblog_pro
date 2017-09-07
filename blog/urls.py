from django.conf.urls import url, include
from .views import index, category, article_detail, archive, author_article, tag_article, awesome_click

app_name = 'blog'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^category/(?P<id>\d+)/$', category, name='category'),
    url(r'^article/(?P<id>\d+)/$', article_detail, name='article'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', archive, name='archive'),
    url(r'^author_article/(?P<id>\d+)/$', author_article, name='author_article'),
    url(r'^tag_article/(?P<id>\d+)/$', tag_article, name='tag_article'),
    url(r'^awesome_click/$', awesome_click, name='awesome_click'),
]