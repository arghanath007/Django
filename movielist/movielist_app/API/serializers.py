from rest_framework import serializers

from movielist_app.models import WatchList, StreamPlatform


#! Model Serializer

class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = "__all__"
