from django.db.models import Q


from users.models import Profile, Skill


def searchProfiles(request):

    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skills = Skill.objects.filter(name__icontains=search_query)

    # profiles = Profile.objects.all()  # Get all the profiles from the database

    # Get all the profiles which matches the 'search query'. 'icontains' is case insensitive. So cases don't matter. 'about__icontains=search_query' is searching in the 'about' field of the 'Profile' model. '|' is the OR operator. 'skill__in=skills' means that does the profile have a skill that's listed in the 'search query'.
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | Q(about__icontains=search_query) | Q(skill__in=skills))

    return profiles, search_query
