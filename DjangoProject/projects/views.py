# Storing all of the views for the 'projects' app.

from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return  HttpResponse("<h1>Projects</h1>")


def project(request, pk):
    return  HttpResponse(f"<h1>Some Specific Project with the id of {pk}</h1>")
