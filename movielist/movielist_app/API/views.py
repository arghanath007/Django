from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from movielist_app.models import Movie
from movielist_app.API.serializers import MovieSerializer

@api_view(['GET','POST'])
def MovieList(request):
    if request.method == 'GET':
        movies=Movie.objects.all()
        # serializer=MovieSerializer(movies)
        serializer=MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
# def MovieDetail(request,self):
def MovieDetail(request,pk):
    
    if request.method == 'GET':
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        movie=Movie.objects.get(pk=pk)
        # movie=Movie.objects.get(pk=self.kwargs.get('pk', None))
        serializer=MovieSerializer(movie)   
        return Response(serializer.data)
    
    if request.method =='PUT':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
        
    if request.method == 'DELETE':
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        