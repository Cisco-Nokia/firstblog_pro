from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# 继承AbstractUser模型，该模型初始有一些基础属性，可自行查看，主要是有用户名和密码
class User(AbstractUser):
    user_img = models.ImageField(upload_to='userimg/%Y/%m', default='userimg/default.jpg', blank=True, verbose_name='用户头像')
    user_website = models.URLField(max_length=100, blank=True, verbose_name='个人网站地址')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username