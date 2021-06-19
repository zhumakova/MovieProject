from django.db import models


class Movie(models.Model):
    title=models.CharField(max_length=100,unique=True)
    poster=models.ImageField()
    description=models.CharField(max_length=500)
    year=models.PositiveIntegerField()
    movie=models.FileField()
    avg_rate=models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class Genre(models.Model):
    title=models.CharField(max_length=100,unique=True)
    genre=models.ManyToManyField('Movie')
