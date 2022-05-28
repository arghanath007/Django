from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# For getting  the 'MEDIA_URL' and 'MEDIA_ROOT' from the 'settings.py' file.

# This will create a new url for the static files.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),

    path('reset_password/', PasswordResetView.as_view(template_name='reset_password.html'),
         name='reset_password'),

    path('reset_password_sent/',
         PasswordResetDoneView.as_view(template_name='reset_password_sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='reset.html'),
         name='password_reset_confirm'),

    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),
         name='password_reset_complete'),

]

# To get the media or static files from the 'static' folder in development mode.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# To get the media or static files from the 'prodstaticfiles' folder in production mode.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
