from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer, LoginSerializer


# Endpoint to handle user registration
class RegisterApi(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.serializer_class.Meta.model.objects.get(pk=response.data['id'])
        token, created = Token.objects.get_or_create(user=user)
        # Return generated token and user ID after successful registration
        return Response({'token': token.key, 'user_id': user.pk}, status=status.HTTP_201_CREATED)


# Endpoint to authenticate users and return a token
class LoginApi(APIView):

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.pk})
        # Return error if authentication fails
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)


# Endpoint to handle user logout and token invalidation
class LogoutApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Invalidate the user's token
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

