from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterAPIView,  TeamViewSet, UserProfileViewSet, UserViewSet, GroupViewSet


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .customToken import MyTokenObtainPairView

router = DefaultRouter()

router.register('team', TeamViewSet)
router.register('profile', UserProfileViewSet)
router.register('user', UserViewSet)
router.register('group', GroupViewSet)

urlpatterns = [
    path('/', include(router.urls)),
    path('/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/refresh_token', TokenRefreshView.as_view(), name='token_refresh'),
    path('/register', RegisterAPIView.as_view()),
]
