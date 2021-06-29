from .models import Rating
from Cinema.models import Movie
def comment_validate(text):
    text=text.lower()
    bad_word='bad'
    if bad_word not in text:
        return True
    return False

def count_average_score(score_list,movie):
    avg_rate=0.0
    amount=len(score_list)
    for obj in score_list:
        avg_rate+=obj.score
    avg_rate/=amount
    movie.avg_rate=avg_rate
    movie.save()