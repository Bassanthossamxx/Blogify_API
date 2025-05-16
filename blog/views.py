from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , viewsets
from django.contrib.auth import authenticate , get_user_model
from .models import CustomUser , Post , Comment
from .serializer import UserSerializer, PostSerializer , CommentSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from social_django.utils import load_backend, load_strategy
from social_core.exceptions import AuthException
from django.conf import settings
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
User = get_user_model()

#User Profile View
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Registration view
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Account created successfully!',
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Login View
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return (Response
                    ({'error': 'Email and password are required'},status=status.HTTP_400_BAD_REQUEST))
        user = authenticate(request, username=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful!',
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

#Logout View
class LogoutView(APIView):
    #JWT tokens logout view
    def post(self, request):
        refresh = request.data.get('refresh')
        if not refresh:
            return Response({'error': 'Refresh token required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Google login view
class GoogleLoginView(APIView):
    def get(self, request):
        google_login_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY}&response_type=code&redirect_uri={settings.SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI}&scope=email%20profile"
        return Response({"login_url": google_login_url}, status=status.HTTP_200_OK)

# Google callback view
class GoogleCallbackView(APIView):
    def post(self, request):
        auth_code = request.data.get('code')
        if not auth_code:
            return Response({'error': 'Authorization code not provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate with Google
        strategy = load_strategy(request)
        backend = load_backend(strategy=strategy, name='google-oauth2', redirect_uri=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI)

        try:
            user = backend.do_auth(auth_code)
        except AuthException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        if user and user.is_active:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful!',
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Authentication failed'}, status=status.HTTP_400_BAD_REQUEST)

class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthorOrReadOnly]

class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthorOrReadOnly]
