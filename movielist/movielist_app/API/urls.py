from django.urls import path, include
# from movielist_app.API.views import MovieList, MovieDetail  # Function Based View
# Class Based View
from movielist_app.API.views import WatchListListAV, WatchListDetailAV, StreamPlatformListAV, SteamPlatformDetailsAV, ReviewList, ReviewDetail, ReviewCreate, Stream_Platform

from rest_framework.routers import DefaultRouter


#! Routers

router = DefaultRouter()
router.register('platform', Stream_Platform,
                basename='StreamPlatform')


urlpatterns = [
    path('list/', WatchListListAV.as_view(), name='Watch-List'),
    path('list/<int:pk>/', WatchListDetailAV.as_view(), name='WatchList-detail'),

    #     path('platform/', StreamPlatformListAV.as_view(), name='StreamPlatform-list'),
    #     path('platform/<int:pk>', SteamPlatformDetailsAV.as_view(),
    #          name='StreamPlatform-detail'),

    path('<int:pk>/create-reviews/',
         ReviewCreate.as_view(), name='Review-Create'),

    path('<int:pk>/reviews/', ReviewList.as_view(), name='Review-list'),

    path('reviews/<int:pk>/',
         ReviewDetail.as_view(), name='Review-list'),


    path('', include(router.urls)),







    # path('reviews/', ReviewListAV.as_view(), name='Review-list'),
    # path('reviews/<int:pk>', ReviewDetailsAV.as_view(), name='Review-detail'),

    # path('review', ReviewList.as_view(), name='Reviews'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='Reviews-detail')

    # path('platform/<int:pk>', SteamPlatformDetailsAV.as_view(),
    #     name='streamplatform-detail'),  # For 'serializers.HyperlinkedModelSerializer'.

]
