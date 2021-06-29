from django.contrib.auth.models import User
from django.db import models

from Cinema.models import Movie


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    score=models.FloatField(default=0.0)