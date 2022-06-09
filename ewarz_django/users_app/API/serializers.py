from rest_framework import serializers
from users_app.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'tc', 'password', 'password2']

        extra_kwargs = {
            'password': {'write_only': True},
        }

    #! Validation password and password2 while registration. This will be called with .is_valid() in views.py file.
    def validate(self, data):

        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


#! User Login Serializer.
class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']
