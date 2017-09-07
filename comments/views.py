from django.shortcuts import render, redirect, reverse
from .forms import CommentForm
from .models import Comment
from blog.models import Article
# Create your views here.


def post_comment(request, id):
    article = Article.objects.get(id=id)
    # print(request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.article = article
            comment_form.username = request.user
            comment_form.save()
            return redirect(reverse('blog:article', kwargs={'id': id}))
        else:
            comment_list = article.comment_set.all()
            context = {'article': article,
                       'form':form,
                       'comment_list':comment_list,
                       }
            return render(request, 'blog/article.html', context=context)
