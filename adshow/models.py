from django.db import models

# Create your models here.

# 定义轮播图模型
class Ad(models.Model):
    title = models.CharField(max_length=20,verbose_name='广告名称')
    desc = models.CharField(max_length=30, verbose_name='广告描述')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    url = models.URLField(verbose_name='广告链接')
    img = models.ImageField(upload_to='ad/%Y/%m', verbose_name='广告图片')
    index = models.IntegerField(default=100, verbose_name='排序(从小到大)')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title