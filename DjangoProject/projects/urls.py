from django.urls import path

from .views import projects, project, createProject

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'), # 'pk' is the primary key. Dynamic Route
    path('create-project/', createProject, name='create-project'),
]
 