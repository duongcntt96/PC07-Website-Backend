from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Chung_loai_viewSet, Danh_muc_kho_viewSet, Danh_muc_nguon_cap_viewSet, Danh_muc_phuong_tien_ViewSet, Chi_tiet_phieu_nhap_ViewSet, Phieu_nhap_ViewSet

router = DefaultRouter()

router.register('chungloai', Chung_loai_viewSet)
router.register('phuongtien', Danh_muc_phuong_tien_ViewSet)
router.register('kho', Danh_muc_kho_viewSet)
router.register('nguoncap', Danh_muc_nguon_cap_viewSet)
router.register('phieunhap', Phieu_nhap_ViewSet)
# router.register('phieuxuat', Phieu_xuat_ViewSet)
router.register('chitietphieunhap', Chi_tiet_phieu_nhap_ViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
