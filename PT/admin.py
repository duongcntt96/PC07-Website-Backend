from django.contrib import admin
from .models import Chung_loai, Chat_luong, Trang_thai, Phuong_tien, Dinh_muc_nhien_lieu, Nhat_trinh_xe
from .models import Image

# Register your models here.
admin.site.register(Phuong_tien)
admin.site.register(Chung_loai)
admin.site.register(Chat_luong)
admin.site.register(Trang_thai)
admin.site.register(Dinh_muc_nhien_lieu)
admin.site.register(Nhat_trinh_xe)

admin.site.register(Image)
