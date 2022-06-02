from rest_framework import serializers

from movielist_app.models import WatchList, StreamPlatform, Review


#! Model Serializer


class ReviewSerializer(serializers.ModelSerializer):

    reviewer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['watchlist']


class WatchListSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    # class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):

    # Created a new field, which contains all the elements regarding the watchlist. If the stream platform selected is 'Netflix' then this contains all the shows, movies which are available on Netflix currently.
    # This is a string related field. which will return whatever this('__str__') functions returns from the model.
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='movie-detail')
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"
