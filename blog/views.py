from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Article, Category, Tag
from users.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from comments.forms import CommentForm
# Create your views here.


# 定义主页的视图函数，主页上的大部分内容都通过我们自定义的模板标签进行了渲染
# 还剩下--左边：文章列表和分页需要我们在这里处理
def index(request):
    article_list = Article.objects.all()
    article_list = page_article(request, article_list)
    context = {
        'article_list': article_list,
    }
    return render(request,'blog/index.html', context=context)


# 定义点击导航栏中分类时的视图函数
def category(request, id):
    article_list = Article.objects.filter(category_id=id)
    article_list = page_article(request, article_list)
    category_result = Category.objects.get(id=id)
    context = {
        'article_list': article_list,
        'category_result': category_result,
    }
    return render(request, 'blog/result-list.html', context=context)


# 每篇文章详情视图函数
def article_detail(request, id):
    article = Article.objects.get(id=id)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
       TocExtension(slugify=slugify),
    ])
    article.content = md.convert(article.content)
    comment_list = article.comment_set.all()
    form = CommentForm()
    context = {
        'article': article,
        'comment_list': comment_list,
        'toc':md.toc,
        'form': form,
    }
    return render(request, 'blog/article.html', context=context)


# 右侧按时间归档的视图函数
def archive(request, year, month):
    article_list = Article.objects.filter(date_publish__year=year, date_publish__month=month)
    article_list = page_article(request, article_list)
    archive_time = year + "年" + month + "月"
    context = {
        'article_list': article_list,
        'archive_time': archive_time,
    }
    return render(request, 'blog/result-list.html', context=context)


# 按照作者名来获取文章，作者与文章之间是一对多的关系
def author_article(request, id):
    user = User.objects.get(id=id)
    article_list = user.article_set.all()
    article_list = page_article(request, article_list)
    context = {
        'article_list': article_list,
        'user': user,
    }
    return render(request, 'blog/result-list.html', context=context)


# 按照标签来获取文章，标签与文章之间是多对多的关系
def tag_article(request, id):
    tag = Tag.objects.get(id=id)
    # tag = get_object_or_404(Tag, id=id)
    article_list = tag.article_set.all()
    article_list = page_article(request, article_list)
    context = {
        'article_list': article_list,
        'tag': tag,
    }
    return render(request, 'blog/result-list.html', context=context)


# 始终牢记这个函数得到的只是某一页文章列表的object
# 这个值传递到templates中去之后，可以调用article.paginator.page_range这样的值
# 这里控制一页显示多少篇文章
def page_article(request, article_list):
    paginator = Paginator(article_list, 5)
    page = request.GET.get('page')
    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)
    return article


def awesome_click(request):
    if request.method == 'GET':
        print(request.GET)
        arti_id = request.GET['article_id']
        print(arti_id)
    awesome = 0
    if arti_id:
        article = Article.objects.get(id=int(arti_id))
        if article:
            awesome = article.awesome_count + 1
            article.awesome_count = awesome
            article.save()
            awesome = '<span class="glyphicon glyphicon-thumbs-up">%s</span>' % (awesome,)

    return HttpResponse(awesome)