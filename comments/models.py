from django.db import models

# Create your models here.

# 定义评论模型，每条评论都属于一个用户，每条评论都只属于一篇文章
class Comment(models.Model):
    username = models.ForeignKey('users.User', verbose_name='评论人')
    content = models.TextField(verbose_name='评论内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    article = models.ForeignKey('blog.Article', verbose_name='评论所属文章')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return str(self.id)