from django.urls import path, include
from rest_framework.routers import DefaultRouter

from PT.api.views import ImageViewSet, PhuongtienViewSet, TeamViewSet, Chungloai_ViewSet, DinhmucnhienlieuViewSet
from PT.api.views import NhattrinhxeViewSet, TrangthaiViewSet, ChatluongViewSet

from PT.api.views import PhuongtienOfToAPIView

router = DefaultRouter()

router.register('phuongtien', PhuongtienViewSet)
router.register('to', TeamViewSet)
router.register('trangthai', TrangthaiViewSet)
router.register('chungloai', Chungloai_ViewSet)
router.register('chatluong', ChatluongViewSet)
router.register('dinhmuc', DinhmucnhienlieuViewSet)
router.register('nhattrinhxe', NhattrinhxeViewSet)
router.register('image', ImageViewSet)


urlpatterns = [
    path('/', include(router.urls)),
    # path('pt', PhuongtienOfToAPIView.as_view()),
]
