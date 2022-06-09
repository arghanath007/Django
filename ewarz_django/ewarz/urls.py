from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('user/', include('users_app.urls')),
    path('api/user/', include('users_app.API.urls')),
]
