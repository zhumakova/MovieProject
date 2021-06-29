from django.http import HttpResponse
from django.shortcuts import render, redirect
from Cinema.models import Movie
from Cinema.forms import *
from .forms import *
from .models import *
from .service import count_average_score
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User



def comment_page(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    comment = movie.comment_set.all()
    form=CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           text=form.cleaned_data.get('text')
           Comment.objects.create(movie=movie,text=text,user=request.user)
    return render(request, 'comment.html', {'movie': movie, 'form': form,'comment':comment})




def rating_page(request, movie_id):
    movie = Movie.objects.get(id=movie_id)

    form=RatingForm()
    if request.method=='POST':
        form = RatingForm(request.POST)
        if form.is_valid():
           score=form.cleaned_data.get('score')
           Rating.objects.create(user=request.user,movie=movie,score=score)

        return redirect('movie_detail')
    return render(request, 'rating.html', {'movie': movie, 'form': form})