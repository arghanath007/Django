from django.urls import path,include
from movielist_app.views import MovieList 
urlpatterns = [
    path('list/', MovieList, name='movie-list'),
]