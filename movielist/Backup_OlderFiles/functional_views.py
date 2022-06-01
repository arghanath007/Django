# # from django.shortcuts import render
# from movielist_app.models import Movie
# from django.http import JsonResponse

# # # Create your views here.


# def MovieList(request):
#     movies = Movie.objects.all()
#     data = {
#         "movies": list(movies.values())
#     }
#     return JsonResponse(data)


# def MovieDetail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     details = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active,
#     }
#     return JsonResponse(details)
