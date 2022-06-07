from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from users_app.API.views import getRoutes, MyTokenObtainPairView, Register


urlpatterns = [
    path('', getRoutes, name='getRoutes'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('register/', Register.as_view(), name='register'),
]
