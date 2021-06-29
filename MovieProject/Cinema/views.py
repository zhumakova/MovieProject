from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from Comments.forms import CommentForm,RatingForm
from Comments.models import Comment

from Comments.service import count_average_score

from Comments.models import Rating


def movies_page(request):
    movies=Movie.objects.all()
    return render(request,'movies.html',{'movies':movies})

def genres_page(request):
    genres=Genre.objects.all()
    return render(request,'genres.html',{'genres': genres})





def movie_detail_page(request,movie_id):
    user = request.user
    movies=Movie.objects.get(id=movie_id)
    genres = Genre.objects.filter(genre=movies)
    comment = movies.comment_set.all()
    score_list=movies.rating_set.all()
    form = CommentForm()
    form1=RatingForm()
    if request.method == 'POST':
        if isinstance(user, AnonymousUser):
            return redirect('login')
        form = CommentForm(request.POST)
        form1=RatingForm(request.POST)
        if form.is_valid() or form1.is_valid():
            text = form.cleaned_data.get('text')
            Comment.objects.create(movie=movies, text=text, user=user)
            score = form.cleaned_data.get('score')
        return redirect('movie_detail')
    count_average_score(score_list,movies)
    return render(request,'movie_detail.html',{'movie':movies,'genres':genres,'form':form,'comment':comment,'form1':form1})


def genre_movies(request,genre_id):
    genre_m=Movie.objects.filter(genre__id=genre_id)
    return render(request,'genre_movies.html',{'genre_m':genre_m})

def register_page(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('You were successfully registered!')
    return render(request,'register.html',{'form':form})


def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        login(request,user)
        return HttpResponse('Вы вошли!')

    return render(request,'login.html')