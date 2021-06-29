from django.urls import path
from .views import *

urlpatterns=[
    path('comment/<int:movie_id>/',comment_page,name='comment'),
    path('score/<int:movie_id>/',rating_page,name='score'),
 ]