from django.urls import path

from users.views import profiles, userAccount, userProfile, loginUser, logoutUser, registerUser, editAccount

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),


    path('', profiles, name='profiles'),
    path('profile/<str:pk>/', userProfile, name='user-profile'),
    path('account/', userAccount, name='user-account'),
    path('edit-account/', editAccount, name='edit-account'),
]
