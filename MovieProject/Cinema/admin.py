from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','year','avg_rate','description']

admin.site.register(Movie,MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Genre,GenreAdmin)