from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path , include
from .views import RegisterView, LoginView , GoogleLoginView, GoogleCallbackView , LogoutView , PostsViewSet
from rest_framework.routers import DefaultRouter
route = DefaultRouter()
route.register(r'post', PostsViewSet , basename="post")
urlpatterns = [
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('register/', RegisterView.as_view(), name='register'),
path('login/', LoginView.as_view(), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),
path('social/', include('social_django.urls', namespace='social')),
    path('', include(route.urls)),

]
#google endpoint : http://localhost:8000/auth/social/login/google-oauth2/