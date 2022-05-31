from rest_framework import serializers

from movielist_app.models import WatchList


#! Model Serializer

class WatchListSerializer(serializers.ModelSerializer):

    # Generating a custom serializer field
    nameLength = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"
        # fields = ['id', 'name', 'description']
        # exclude = ['id']

    # 'obj' is the movie object which can access to all the fields of the model.
    # def get_nameLength(self, obj):
    #     length = len(obj.name)
    #     return length


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError(
#             "Name must be at least 2 characters long")


#! Serializer
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])  # validators
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # 'value' is the value which is stored in the 'name' field.
#     #! Field Level Validation
#     # def validate_name(self, value):

#     #     if len(value) < 2:
#     #         raise serializers.ValidationError(
#     #             "Name must be at least 2 characters long.")

#     #     return value

#     #! Object Level Validation
#     def validate(self, value):
#         if value['name'] == value['description']:
#             raise serializers.ValidationError(
#                 "Title and description must be different.")

#         return value
