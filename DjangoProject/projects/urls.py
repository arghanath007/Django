from django.urls import path

from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='Some_Project'), # 'pk' is the primary key. Dynamic Route
]
 