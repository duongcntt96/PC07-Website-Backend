from django.db import models

from profiles.models import Team


class Chung_loai(models.Model):
    stt = models.IntegerField(null=True, blank=True)
    ten = models.CharField(max_length=200, null=True)
    mo_ta = models.CharField(max_length=500, null=True, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.RESTRICT, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['stt']

    def __str__(self):
        if self.parent != None:
            return str(self.stt) + '. ' + str(self.parent) + '--' + self.ten
        return self.ten
# Chất lượng


class Chat_luong(models.Model):
    chat_luong = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chat_luong
# Trạng thái


class Trang_thai(models.Model):
    trang_thai = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trang_thai


class Phuong_tien(models.Model):
    ten = models.CharField(max_length=200)

    chung_loai = models.ForeignKey(
        Chung_loai, related_name='phuongtien_list', on_delete=models.RESTRICT, default=5)

    def chung_loai__ten(self):
        return self.chung_loai.ten

    don_vi_tinh = models.CharField(max_length=50, null=True, blank=True)
    so_luong = models.IntegerField(null=True, blank=True)
    nhan_hieu = models.CharField(max_length=200, null=True, blank=True)
    so_khung = models.CharField(max_length=20, null=True, blank=True)
    so_may = models.CharField(max_length=20, null=True, blank=True)
    so_dong_co = models.CharField(max_length=20, null=True, blank=True)
    bien_so = models.CharField(max_length=11, null=True, blank=True)
    trang_thai = models.ForeignKey(
        Trang_thai, on_delete=models.RESTRICT, default=5, null=True, blank=True)

    def trang_thai__ten(self):
        return self.trang_thai.trang_thai

    chat_luong = models.ForeignKey(
        Chat_luong, on_delete=models.RESTRICT, default=1, null=True, blank=True)

    def chat_luong__ten(self):
        if (self.chat_luong):
            return self.chat_luong.chat_luong
        return ''

    # models.ForeignKey(Noi_bo_tri, on_delete=models.RESTRICT, default=1)
    noi_bo_tri = models.ForeignKey(
        'self', on_delete=models.RESTRICT, null=True, blank=True)

    def noi_bo_tri__ten(self):
        if (self.noi_bo_tri):
            return self.noi_bo_tri.ten
        return ''

    quan_ly = models.ForeignKey(
        Team, on_delete=models.RESTRICT, null=True, blank=True)

    def quan_ly__name(self):
        if (self.quan_ly):
            return self.quan_ly.name
        return ''

    nguon_cap = models.CharField(max_length=50, null=True, blank=True)
    # file_nguon_cap = models.FileField(upload_to='static/files',null=True)
    thoi_gian_nhan = models.CharField(max_length=10, null=True, blank=True)
    thoi_gian_san_xuat = models.CharField(max_length=10, null=True, blank=True)
    thoi_gian_dua_vao_hoat_dong = models.CharField(
        max_length=10, null=True, blank=True)

    order = models.IntegerField(null=True, blank=True)

    def hinh_anh(self):
        if self.image_set.all():
            return self.image_set.all()[0].hinh_anh.url
        return None

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return self.ten
    # def ordered_by_chung_loai(self):
    # 	return self.phuong_tien_set.all().order_by('-chung_loai__ten')


class Dinh_muc_nhien_lieu(models.Model):
    phuong_tien = models.ForeignKey(
        Phuong_tien, primary_key=True, on_delete=models.CASCADE)
    # Nổ máy
    dinh_muc_1 = models.FloatField(null=True, blank=True)
    # Chạy đường dài
    dinh_muc_2 = models.FloatField(null=True, blank=True)
    # Vận hành hệ thống chuyên dùng (bơm/thang/cẩu)
    dinh_muc_3 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.phuong_tien.ten


class Nhat_trinh_xe(models.Model):
    phuong_tien = models.ForeignKey(Phuong_tien, on_delete=models.CASCADE)
    thoi_gian = models.DateField(null=True)
    km_luc_di = models.IntegerField(null=True)
    km_luc_ve = models.IntegerField(null=True)
    noi_dung_cong_tac = models.CharField(max_length=200, null=True, blank=True)
    noi_den_cong_tac = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.phuong_tien.ten


class Image(models.Model):
    phuong_tien = models.ForeignKey(Phuong_tien, on_delete=models.PROTECT)
    hinh_anh = models.ImageField(
        upload_to='static/images/upload/', null=True, blank=True)
