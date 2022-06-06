from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


from user_app.API.serializers import RegistrationSerializer

#! This import is needed to generate the token when user registers.
# from user_app.models import create_auth_token


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':

        serializer = RegistrationSerializer(data=request.data)

        context = {}

        if serializer.is_valid():
            account = serializer.save()  # Storing and accessing Account data

            context['response'] = 'Account created successfully'
            context['username'] = account.username
            context['email'] = account.email

            #! Authentication Token of the user which is created.  For Token Authentication.
            # token = Token.objects.get(user=account).key

            # context['token'] = token

            #! Creating Token Manually. For JWT Authentication.

            refresh = RefreshToken.for_user(account)

            context['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

        else:
            context['error'] = serializer.errors

        return Response(context)


@api_view(['POST'])
def logout_view(request):

    # 'user' is the currently logged in user.
    if request.method == 'POST':
        request.user.auth_token.delete()  # Delete the token of the user.
        return Response(status=status.HTTP_200_OK)
