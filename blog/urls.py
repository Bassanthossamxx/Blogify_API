from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path , include
from .views import RegisterView, LoginView , GoogleLoginView, GoogleCallbackView , LogoutView , PostsViewSet , CommentsViewSet
from rest_framework.routers import DefaultRouter
route = DefaultRouter()
route.register(r'post', PostsViewSet , basename="post")
route.register(r'comment', CommentsViewSet , basename="comment")
urlpatterns = [
path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('auth/register/', RegisterView.as_view(), name='register'),
path('auth/login/', LoginView.as_view(), name='login'),
path('auth/logout/', LogoutView.as_view(), name='logout'),
# path('auth/social/', include('social_django.urls', namespace='social')),
    path('api/', include(route.urls)),

]
#google endpoint : http://localhost:8000/auth/social/login/google-oauth2/