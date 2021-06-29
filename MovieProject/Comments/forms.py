from django import forms
from .models import *


class CommentForm(forms.Form):
    text = forms.CharField(max_length=200)
class RatingForm(forms.Form):
    score=forms.FloatField(min_value=1.0,max_value=10.0)