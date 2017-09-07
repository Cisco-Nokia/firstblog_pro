from django.contrib import admin
from .models import Category, Tag, Article, Link
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','index']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['title','url','index']
    list_editable = ['index']


class ArticleAdmin(MarkdownxModelAdmin):
    list_display = ['title', 'date_publish', 'author','recommend_index', 'click_count']
    list_editable = ['recommend_index']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Link, LinkAdmin)
