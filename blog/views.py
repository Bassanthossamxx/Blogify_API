from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

#User endpoints:
class AuthViewSet(ViewSet):

   # Registration endpoint
   @action(detail=False, methods=['post'])
   def register(self, request):
     serializer = UserSerializer(data=request.data)
     if serializer.is_valid():
         user = serializer.save()
         user.set_password(serializer.validated_data['password'])  # Hash the password
         user.save() #Save after Hashing password
         return Response(
             {'message': 'Account created successfully!',},status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Login endpoint
   @action(detail=False, methods=['post'])
   def login(self, request):
     username = request.data.get('username')
     password = request.data.get('password')
     user = authenticate(username=username, password=password)
     if user:
         #generate refresh token
         refresh = RefreshToken.for_user(user)
         return Response({
             'message': 'Login successful!',
             'access': str(refresh.access_token),
             'refresh': str(refresh),
         }, status=status.HTTP_200_OK)
     return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
