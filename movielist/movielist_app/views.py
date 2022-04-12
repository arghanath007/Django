from django.shortcuts import render
from movielist_app.models import Movie
from django.http import JsonResponse

# Create your views here.

def MovieList(request):
    movies=Movie.objects.all()
    data={
            "movies":list(movies.values())
        }
    return JsonResponse(data)
    
