from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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


def paginateProfiles(request, profiles, results):

    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)

    except EmptyPage:
        page = paginator.num_pages  # Giving us the count of the last page.
        profiles = paginator.page(page)

    left_index = (int(page) - 4)
    right_index = (int(page) + 5)

    if left_index < 1:
        left_index = 1

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, profiles
