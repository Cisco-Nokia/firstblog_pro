from django.db import models
from django.utils.html import strip_tags
from markdownx.models import MarkdownxField

# Create your models here.


# 定义文章分类，有一个排序字段，用于自定义文章在导航条上的显示顺序
# 一篇文章对应一个分类，一个分类可以有多篇文章
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=50, verbose_name='分类排序')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'name']


# 定义标签，一个文章可以有多个标签，一个标签也可以对应多篇文章
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


# 定义文章，文章所属作者与usersAPP中的User关联
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=100, blank=True, verbose_name='文章描述')
    # content = models.TextField(verbose_name='文章内容')
    content = MarkdownxField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    awesome_count = models.IntegerField(default=0, verbose_name='点赞数')
    recommend_index = models.IntegerField(default=100, verbose_name='推荐顺序')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    author = models.ForeignKey('users.User', verbose_name='作者')
    category = models.ForeignKey(Category, blank=True, verbose_name='所属分类')
    tag = models.ManyToManyField(Tag, verbose_name='所属标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.title

    def save(self):
        if not self.desc:
            self.desc = strip_tags(self.content)[:54]
        super(Article, self).save()


# 友情链接
class Link(models.Model):
    title = models.CharField(max_length=50, verbose_name="链接标题")
    desc = models.CharField(max_length=200, verbose_name="链接描述")
    url = models.URLField(verbose_name="链接地址")
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    index = models.IntegerField(default=999, verbose_name="排序（从小到大）")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.title
