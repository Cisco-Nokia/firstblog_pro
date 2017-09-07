from django.conf.urls import url
from .views import register

app_name = 'user'
urlpatterns = [
    url(r'^register/$', register, name='register'),
]