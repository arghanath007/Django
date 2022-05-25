# Storing all of the views for the 'projects' app.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator


from projects.models import Project
from projects.forms import ProjectForm
from projects.utils import searchProjects, paginateProjects


# To see all the projects

def projects(request):

    # projects = Project.objects.all()  # To get all the projects

    projects, search_query = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 1)

    context = {
        'projects': projects,
        'search': search_query,
        'custom_range': custom_range,
    }
    return render(request, "projects/projects.html", context)


# To view a Single Project

def project(request, pk):
    # To get the project with the id(pk)
    projectObj = Project.objects.get(id=pk)
    # tags=projectObj.tags.all() # To get the tags of the project
    return render(request, "projects/single-project.html", {'project': projectObj})


# Create a New Project
# Sending/redirecting the user back to the login page if they are not logged in.
@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    # Getting the currently logged in user.
    profile = request.user.profile
    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():

            # Instance of the current project
            project = form.save(commit=False)

            # Connecting the newly created project to the logged in user.
            project.owner = profile
            project.save()

            # Redirecting the user back to the 'projects' page.
            return redirect('user-account')

    context = {
        'form': form,
    }
    return render(request, "projects/project_form.html", context)


# To update a Project
@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    # Getting the projects of the logged in user only.
    project = profile.project_set.get(id=pk)
    # Prefill all the form fields with the data of the project
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # To update the project with the new data
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid:
            form.save()
            return redirect('user-account', pk=pk)

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


# To delete a Project
@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    # Only the owner/logged in user can delete the project.
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {
        'object': project,
    }
    return render(request, 'delete_template.html', context)
