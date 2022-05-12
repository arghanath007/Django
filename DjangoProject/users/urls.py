from django.urls import path

from users.views import profiles, userProfile

urlpatterns = [
    path('', profiles, name='profiles'),
    path('profile/<str:pk>/', userProfile, name='user-profile'),
]
