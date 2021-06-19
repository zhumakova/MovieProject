from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def movies_page(request):
    movies=Movie.objects.all()
    return render(request,'movies.html',{'movies':movies})

def genres_page(request):
    genres=Genre.objects.all()
    return render(request,'genres.html',{'genres': genres})

def movie_detail_page(request,movie_id):
    movies=Movie.objects.get(id=movie_id)
    genres = Genre.objects.filter(genre=movies)
    return render(request,'movie_detail.html',{'movie':movies,'genres':genres})


def genre_movies(request,genre_id):
    genre_m=Movie.objects.filter(genre__id=genre_id)
    return render(request,'genre_movies.html',{'genre_m':genre_m})