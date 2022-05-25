from gettext import install
import imp
import sqlite3
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


from users.models import Profile
from users.forms import CustomUserCreationForm, ProfileForm, SkillForm

from users.utils import searchProfiles, paginateProfiles


def loginUser(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'Username does not exist')

        # 'authenticate()' will take the 'username' and the 'password' and it will male sure that the password matches the 'username'. It will return either the 'user' instance or 'None'.
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 'login()' create a session for the user in the database.
            login(request, user)
            return redirect('profiles')

        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'users/login_register.html')


def logoutUser(request):

    # This is going to delete the session of the logged in user.
    logout(request)
    messages.info(request, 'User was logged out successfully')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Gives us an instance of the form but doesn't save it to the database.
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User was created successfully')
            login(request, user)
            return redirect('edit-account')

        else:
            messages.error(request, 'Error occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def profiles(request):

    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request, profiles, 1)

    context = {
        'profiles': profiles,
        'search': search_query,
        'custom_range': custom_range
    }
    return render(request, 'users/profiles.html', context)


# Function Based View
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {
        'profile': profile,
        'topSkills': topSkills,
        'otherSkills': otherSkills
    }
    return render(request, 'users/user-profile.html', context)


@ login_required(login_url='login')
def userAccount(request):

    # Get the profile of the logged in user. Using the One to One relationship
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile,
               'skills': skills,
               'projects': projects,
               }
    return render(request, 'users/account.html', context)


@ login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    # Instance is the profile of the logged in user. This will prefill the form with the data of the logged in user.
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        # 'request.FILES' For processing images in forms.
        form = ProfileForm(request.POST, request.FILES,
                           instance=profile)

        if form.is_valid():
            form.save()
            return redirect('user-account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@ login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()
    context = {'form': form}
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():

            # Linking the current skill to the profile of the logged in user.
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!!!')
            return redirect('user-account')
    return render(request, 'users/skill_form.html', context)


@ login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)  # Get the skill we want to update.
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!!!')
            return redirect('user-account')
    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@ login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)  # Get the skill we want to delete.

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was successfully deleted!!!')
        return redirect('user-account')
    context = {'object': skill}
    return render(request, 'delete_template.html', context)
