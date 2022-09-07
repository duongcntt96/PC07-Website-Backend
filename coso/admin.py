from django.contrib import admin

# Register your models here.

from .models import Dia_ban, Coso, Loai_hinh_co_so, Huan_luyen

admin.site.register(Dia_ban)
admin.site.register(Coso)
admin.site.register(Loai_hinh_co_so)
admin.site.register(Huan_luyen)
