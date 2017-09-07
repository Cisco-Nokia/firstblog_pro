from django.contrib import admin
from .models import Ad

# Register your models here.


class AdAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','index']

admin.site.register(Ad,AdAdmin)