from django.shortcuts import render


from users.models import Profile


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
