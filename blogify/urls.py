from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path , include
from blog.views import RegisterView, LoginView , GoogleLoginView, GoogleCallbackView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('auth/', include('social_django.urls', namespace='social')),  # Include social authentication URLs

]
#google endpoint : http://localhost:8000/auth/login/google-oauth2/
