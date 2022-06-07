from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    # Can only send information about 'password2' field. Cannot read it.
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        # 'password2' is a field that is not in the build-in 'User' model but others('username', 'email', 'password') are. 'password2' is confirm password.
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Overriding the .save  method of ModelSerializer and adding more functionality/validation to it. ' account = serializer.save()' is calling this function.
    def save(self):

        # Checking if both the password are same or not.
        password = self.validated_data['password']
        confirmPassword = self.validated_data['password2']

        if password != confirmPassword:
            raise serializers.ValidationError(
                {'error': 'Passwords must match'})

        # Another User with the same Email already exists in the database, which we don't want. So, we will not allow this user to register with this duplicate/already existing email from the database.
        matchingEmail = User.objects.filter(email=self.validated_data['email'])

        # Checking if the 'Email' is already registered or not.
        if matchingEmail.exists():
            raise serializers.ValidationError(
                {'error': 'Email already exists'})

        # Creating User Manually.
        account = User(
            email=self.validated_data['email'], username=self.validated_data['username'])

        account.set_password(password)
        account.save()
        return account
