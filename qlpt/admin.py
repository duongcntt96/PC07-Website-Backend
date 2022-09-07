from django.contrib import admin
from .models import Chung_loai, Danh_muc_phuong_tien, Danh_muc_kho, Danh_muc_nguon_cap, Phieu_nhap, Chi_tiet_phieu_nhap
# from .models import Phieu_xuat, Chi_tiet_phieu_xuat
from .models import Sua_chua
admin.site.register(Danh_muc_phuong_tien)
admin.site.register(Danh_muc_kho)
admin.site.register(Danh_muc_nguon_cap)
admin.site.register(Chung_loai)
# admin.site.register(Phieu_xuat)
# admin.site.register(Chi_tiet_phieu_xuat)
admin.site.register(Phieu_nhap)
admin.site.register(Chi_tiet_phieu_nhap)

admin.site.register(Sua_chua)
# Register your models here.
