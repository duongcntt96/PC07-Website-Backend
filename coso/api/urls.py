from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CosoViewSet, DiabanViewSet, LoaihinhcosoViewSet, HuanluyenViewSet

router = DefaultRouter()

router.register('coso', CosoViewSet)
router.register('diaban', DiabanViewSet)
router.register('loaihinh', LoaihinhcosoViewSet)
router.register('huanluyen', HuanluyenViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
