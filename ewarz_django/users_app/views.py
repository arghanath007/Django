# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken


# from users_app.serializers import RegistrationSerializer


# @api_view(['POST'])
# def registerUser(request):
#     if request.method == 'POST':

#         serializer = RegistrationSerializer(data=request.data)

#         context = {}

#         if serializer.is_valid():
#             account = serializer.save()

#             context['response'] = 'Registration Successful'
#             context['username'] = account.username
#             context['email'] = account.email

#             refresh = RefreshToken.for_user(account)

#             context['token'] = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }

#         else:
#             context['error'] = serializer.errors

#         return Response(context)


# @api_view(['POST'])
# def logoutUser(request):

#     if request.method == 'POST':
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
