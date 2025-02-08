from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter

from blog.views import UserAuthViewSet

routers = DefaultRouter()
routers.register('auth', UserAuthViewSet, basename='auth')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(routers.urls)),
]

