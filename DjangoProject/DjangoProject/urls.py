from django.contrib import admin
from django.urls import path, include

# For getting  the 'MEDIA_URL' and 'MEDIA_ROOT' from the 'settings.py' file.
from django.conf import settings

# This will create a new url for the static files.
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),

]

# To get the media or static files from the 'static' folder in development mode.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# To get the media or static files from the 'prodstaticfiles' folder in production mode.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
