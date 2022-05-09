# Storing all of the views for the 'projects' app.

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Project
from .forms import ProjectForm


# To see all the projects

def projects(request):
    projects = Project.objects.all()  # To get all the projects
    context = {
        'projects': projects,
    }
    return render(request, "projects/projects.html", context)


# To view a Single Project

def project(request, pk):
    # To get the project with the id(pk)
    projectObj = Project.objects.get(id=pk)
    # tags=projectObj.tags.all() # To get the tags of the project
    return render(request, "projects/single-project.html", {'project': projectObj})


# Create a New Project

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirecting the user back to the 'projects' page.
            return redirect('projects')

    context = {
        'form': form,
    }
    return render(request, "projects/project_form.html", context)


# To update a Project

def updateProject(request, pk):
    project = Project.objects.get(id=pk)  # To get the project with the id(pk)
    # Prefill all the form fields with the data of the project
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # To update the project with the new data
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid:
            form.save()
            return redirect('project', pk=pk)

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


# To delete a Project

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {
        'object': project,
    }
    return render(request, 'projects/delete_template.html', context)
