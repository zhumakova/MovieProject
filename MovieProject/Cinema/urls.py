from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns=[
     path('movies/',movies_page,name='movies'),
     path('movie_detail/<int:movie_id>/',movie_detail_page,name='movie_detail'),
     path('',genres_page,name='genres'),
     path('genre_movies/<int:genre_id>/',genre_movies,name='genre_movies'),
     path('register/',register_page,name='register'),
     path('login/',login_page,name='login'),
]