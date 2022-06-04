from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    # Can only send password2. Cannot read it.
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        # 'password2' is a field that is not in the build-in 'User' model. 'password2' is confirm password.
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):

        # Checking if both the password are same or not.
        password = self.validated_data['password']
        confirmPassword = self.validated_data['password2']

        if password != confirmPassword:
            raise serializers.ValidationError(
                {'error': 'Passwords must match'})

        # Checking if the 'Email' is already registered or not.
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'error': 'Email already exists'})

        account = User(
            email=self.validated_data['email'], username=self.validated_data['username'])

        account.set_password(password)
        account.save()
        return account
