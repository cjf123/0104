from django.contrib import admin

# Register your models here.

from app.models import *

class New(admin.ModelAdmin):
    list_display = ('title','summary','url','ctime','nt','favor_count','comment_count',)


class User(admin.ModelAdmin):
    list_display = ("username",'password','email','ctime')

class Comments(admin.ModelAdmin):
    list_display = ('news',)

class Collectionadmin(admin.ModelAdmin):
    list_display = ('news',)


# admin.site.register(SendMsg)
admin.site.register(UserInfo, User)
admin.site.register(News, New)
admin.site.register(Comment)
admin.site.register(Collection,Collectionadmin)
