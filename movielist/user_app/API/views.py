from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


from user_app.API.serializers import RegistrationSerializer

# This import is needed to generate the token when user registers.
from user_app.models import create_auth_token


@api_view(['GET', 'POST'])
def registration_view(request):

    if request.method == 'POST':

        serializer = RegistrationSerializer(data=request.data)

        context = {}

        if serializer.is_valid():
            account = serializer.save()  # Storing and accessing Account data

            context['response'] = 'Account created successfully'
            context['username'] = account.username
            context['email'] = account.email

            # Authentication Token of the user which is created.
            token = Token.objects.get(user=account).key

            context['token'] = token

        else:
            context = serializer.errors

        return Response(context)
