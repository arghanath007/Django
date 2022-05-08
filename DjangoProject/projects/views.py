# Storing all of the views for the 'projects' app.

from django.shortcuts import render
from django.http import HttpResponse

from .models import Project
from .forms import ProjectForm


def projects(request):
    projects=Project.objects.all() # To get all the projects
    context={
        'projects': projects,
    }
    return  render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj=Project.objects.get(id=pk) # To get the project with the id(pk)
    # tags=projectObj.tags.all() # To get the tags of the project
    return  render(request, "projects/single-project.html",{'project':projectObj})


def createProject(request):
    form= ProjectForm()
    context={
        'form': form,
    }
    return render(request, "projects/project_form.html",context)