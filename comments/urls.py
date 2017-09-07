from django.conf.urls import url
from .views import post_comment

app_name = 'comments'
urlpatterns = [
    url(r'^article/(?P<id>\d+)/$', post_comment, name='comment'),
]