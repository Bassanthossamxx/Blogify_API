from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter

from blog.views import UserViewSet

routers = DefaultRouter()
# routers.register('posts', PostViewSet)
# routers.register('comments', CommentViewSet)
routers.register('users', UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(routers.urls))
]

