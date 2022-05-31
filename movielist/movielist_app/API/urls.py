from django.urls import path, include
# from movielist_app.API.views import MovieList, MovieDetail  # Function Based View
# Class Based View
from movielist_app.API.views import WatchListListAV, WatchListDetailAV, StreamPlatformListAV


urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),

    path('platform/', StreamPlatformListAV.as_view(), name='platform-list'),

]
