from django.urls import path

from .views import projects, project, createProject, updateProject, deleteProject

urlpatterns = [
    # To see all the projects
    path('', projects, name='projects'),

    # 'pk' is the primary key. Creates a Dynamic Route. To view a Single Project
    path('project/<str:pk>/', project, name='project'),

    # To create a new Project
    path('create-project/', createProject, name='create-project'),

    # To update a Project
    path('update-project/<str:pk>/', updateProject, name='update-project'),

    # To delete a Project

    path('delete-project/<str:pk>/', deleteProject, name='delete-project'),
]
