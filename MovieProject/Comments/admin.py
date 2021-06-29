from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','movie','date_created','text']

admin.site.register(Comment,CommentAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ['user','movie','score']

admin.site.register(Rating,RatingAdmin)