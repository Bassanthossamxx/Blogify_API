from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path , include
from .views import SignUpView, LoginView , GoogleLoginView, GoogleCallbackView

urlpatterns = [
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('signup/', SignUpView.as_view(), name='signup'),
path('login/', LoginView.as_view(), name='login'),
path('auth/', include('social_django.urls', namespace='social')),
]
#google endpoint : http://localhost:8000/auth/login/google-oauth2/