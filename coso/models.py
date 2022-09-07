from django.db import models


class Dia_ban(models.Model):
    ten = models.CharField(max_length=200)
    mota = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.ten


class Loai_hinh_co_so(models.Model):
    ten = models.CharField(max_length=200)
    mota = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.ten


class Coso(models.Model):
    ten = models.CharField(max_length=200)
    dia_ban = models.ForeignKey(
        Dia_ban, blank=True, null=True, on_delete=models.RESTRICT)
    dia_chi = models.CharField(max_length=500)
    sdt = models.CharField(max_length=11, blank=True, null=True)
    co_quan_quan_ly = models.CharField(max_length=200, blank=True, null=True)
    sdt_co_quan_quan_ly = models.CharField(
        max_length=11, blank=True, null=True)
    loai_hinh_co_so = models.ForeignKey(
        Loai_hinh_co_so, blank=True, null=True, on_delete=models.RESTRICT)
    nganh_nghe = models.CharField(
        max_length=200, blank=True, null=True)
    thuoc_phu_luc_2 = models.BooleanField(default=False)
    dang_hoat_dong = models.BooleanField(default=True)

    def diaban(self):
        return self.dia_ban.ten

    def loaihinhcoso(self):
        return self.loai_hinh_co_so.ten

    def __str__(self):
        return self.ten

################### Huấn luyện ##################


class Huan_luyen(models.Model):
    TRANG_THAI_CHOICES = [
        (1, 'Tiếp nhận'),
        (2, 'Đã xây dựng kế hoạch'),
        (3, 'Kết thúc'),
        (4, 'Tạm ngưng'),
        (5, 'Hủy'),
    ]
    TYPE_CHOICES = [
        (1, 'PCCC'),
        (2, 'CNCH'),
    ]

    loai = models.IntegerField(
        choices=TYPE_CHOICES,
        default=1,
    )

    trang_thai = models.IntegerField(
        choices=TRANG_THAI_CHOICES,
        default=1,
    )

    co_so = models.ManyToManyField(Coso, blank=True, null=True)

    ngay_de_nghi = models.DateField(blank=True, null=True)
    ngay_huan_luyen = models.DateField(blank=True, null=True)
    ngay_cap_giay = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.ngay_de_nghi)
