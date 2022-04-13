from django.urls import path,include
from movielist_app.API.views import MovieList, MovieDetail
urlpatterns = [
    path('list/', MovieList, name='movie-list'),
    path('<int:pk>', MovieDetail, name='movie-detail'),
]