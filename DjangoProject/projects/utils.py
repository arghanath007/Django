from django.db.models import Q

from projects.models import Project, Tag


def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    # 'tags__in=tags' means that the project has a tag that's listed in the 'search query'.
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) | Q(description__icontains=search_query) | Q(owner__name__icontains=search_query) | Q(tags__in=tags))

    return projects, search_query
