from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
# from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

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


class ReviewList(generics.ListAPIView):

    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # Only authenticated users can access this view
    permission_classes = [IsAuthenticated]

    # Overriding the default queryset. 'pk' is the primary key of the entertainment(WatchList) Model.
    def get_queryset(self):
        pk = self.kwargs['pk']
        reviews = Review.objects.filter(watchlist=pk)
        return reviews


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReviewCreate(generics.CreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']

        # Getting the WatchList object for which we are writing the review.
        watchlist = WatchList.objects.get(pk=pk)

        currentUser = self.request.user  # Currently logged in user.
        currentUserReviewed = Review.objects.filter(
            watchlist=watchlist, reviewer=currentUser)

        # Restricting the Reviewer to write only one review per WatchList.
        if currentUserReviewed.exists():
            raise ValidationError(
                f'You have already reviewed {watchlist.title} ')

        serializer.save(watchlist=watchlist, reviewer=currentUser)

    def get_queryset(self):
        return Review.objects.all()


#! ModelViewSet

class Stream_Platform(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


#! viewsets and Routers

# class Stream_Platform(viewsets.ViewSet):

#     def list(self, request):  # Get All the Streaming Platforms

#         streamPlatforms = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(streamPlatforms, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):  # Get details of a particular Streaming Platform

#         streamPlatforms = StreamPlatform.objects.all()
#         streamPlatform = get_object_or_404(streamPlatforms, pk=pk)
#         serializer = StreamPlatformSerializer(streamPlatform)
#         return Response(serializer.data)

#     def create(self, request):
#         serialize = StreamPlatformSerializer(data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data)

#         else:
#             return Response(serialize.errors)


#! ReadOnlyModelViewSet
# class Stream_Platform(viewsets.ReadOnlyModelViewSet):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer


#! Generic APIView and Mixins

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
