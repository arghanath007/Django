from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics
from rest_framework.views import APIView

from movielist_app.models import WatchList, StreamPlatform, Review
from movielist_app.API.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer


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
        serializer = StreamPlatformSerializer(
            platforms, many=True, context={'request': request})
        # serializer = StreamPlatformSerializer(
        #     platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SteamPlatformDetailsAV(APIView):

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(
            platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):

        # The particular 'platform' object which we want to update.
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def delete(self, request, pk):

        # The particular 'entertainment' object which we want to delete.
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewListAV(APIView):

    def get(self, request):

        reviews = Review.objects.all()
        serializer = ReviewSerializer(
            reviews, many=True, context={'request': request})
        # serializer = StreamPlatformSerializer(
        #     platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailsAV(APIView):

    def get(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(
            review, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):

        # The particular 'platform' object which we want to update.
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def delete(self, request, pk):

        # The particular 'entertainment' object which we want to delete.
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # Overriding the default queryset.
    def get_queryset(self):
        pk = self.kwargs['pk']
        reviews = Review.objects.filter(watchlist=pk)
        return reviews


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# 'mixins.ListModelMixin' for performing GET operations. 'mixins.CreateModelMixin' for performing POST operations.
# class ReviewList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):

#     queryset = Review.objects.all()  # Storing all the objects.
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
