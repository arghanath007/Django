from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


from users.models import Profile


def loginUser(request):

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
    messages.error(request, 'User was logged out successfully')
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()  # Get all the profiles from the database
    context = {
        'profiles': profiles
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
