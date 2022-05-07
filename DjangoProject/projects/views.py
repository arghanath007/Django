# Storing all of the views for the 'projects' app.

from django.shortcuts import render
from django.http import HttpResponse

projectList=[{
        'id':'1',
        'title': 'E-commerce Website',
        'description': 'This is a e-commerce website',
    },{
        'id':'2',
        'title': 'Portfolio Website',
        'description': 'My Personal Portfolio Website',
    },{
        'id':'3',
        'title': 'Social Media Website',
        'description': 'Some Random Open Source Social Media Website',
    },]


def projects(request):
    msg= 'This is the projects page'
    number=10
    
    context={
        'message':msg,
        'number': number,
        'projects': projectList,
    }
    return  render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj=None
    
    for i in projectList:
        if i['id']==pk:
            projectObj=i
    return  render(request, "projects/single-project.html",{'project':projectObj})
