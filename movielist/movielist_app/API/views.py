from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from movielist_app.models import WatchList, StreamPlatform
from movielist_app.API.serializers import WatchListSerializer, StreamPlatformSerializer


#! Class Based View
class WatchListListAV(APIView):

    def get(self, request):
        watchList = WatchList.objects.all()
        serializer = WatchListSerializer(watchList, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchListDetailAV(APIView):

    def get(self, request, pk):
        try:
            entertainment = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Entertainment not found'}, status=status.HTTP_404_NOT_FOUND)
        entertainment = WatchList.objects.get(pk=pk)
        # entertainment=entertainment.objects.get(pk=self.kwargs.get('pk', None))
        serializer = WatchListSerializer(entertainment)
        return Response(serializer.data)

    def put(self, request, pk):

        # The particular 'entertainment' object which we want to update.
        entertainment = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(entertainment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def delete(self, request, pk):

        # The particular 'entertainment' object which we want to delete.
        entertainment = WatchList.objects.get(pk=pk)
        entertainment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformListAV(APIView):

    def get(self, request):

        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
