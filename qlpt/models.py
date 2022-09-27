import re
from tabnanny import verbose
from time import strftime
from wsgiref.handlers import format_date_time
from django.db import models
from numpy import maximum

# from qlpt.utils import doc_replace


class Chung_loai(models.Model):
    maso = models.CharField(verbose_name='Mã số',
                            max_length=10, null=True, blank=True)
    ten = models.CharField(verbose_name='Tên', max_length=500, null=True)
    mo_ta = models.CharField(
        verbose_name='Mô tả', max_length=500, null=True, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.RESTRICT, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.maso == None:
            length = len(self.parent.chung_loai_set.all())
            if length > 8:
                __maso = str(length+1)
            else:
                __maso = '0'+str(length+1)
            # Khởi tạo mã số phương tiện theo mã nhóm phương tiện
            self.maso = self.parent.maso + __maso
        super(Chung_loai, self).save(*args, **kwargs)

    class Meta:
        ordering = ['maso']
        verbose_name = 'Chủng loại'
        verbose_name_plural = 'Chủng loại'

    def __str__(self):
        if self.maso != None:
            return str(self.maso) + ' - ' + self.ten
        return self.ten


class Danh_muc_phuong_tien(models.Model):
    ten = models.CharField(
        verbose_name='Tên', max_length=200, null=True, blank=True)
    chung_loai = models.ForeignKey(
        Chung_loai, verbose_name='Chủng loại', on_delete=models.RESTRICT, null=True, blank=True)

    hinh_anh = models.FileField(
        verbose_name='Hình ảnh', upload_to="static", null=True, blank=True)

    file = models.FileField(
        verbose_name='File liên quan', upload_to="static", null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)

    def totals(self):
        from django.db.models import Sum
        nhap = Chi_tiet_phieu_nhap.objects.filter(
            phuong_tien=self, phieu_nhap__success=True, phieu_nhap__kho_nhap__active=True, phieu_nhap__kho_nhap__isnull=False).aggregate(Sum('so_luong'))['so_luong__sum']
        xuat = Chi_tiet_phieu_nhap.objects.filter(
            phuong_tien=self, phieu_nhap__success=True, phieu_nhap__kho_xuat__isnull=False).aggregate(Sum('so_luong'))['so_luong__sum']
        if nhap:
            if xuat:
                nhap -= xuat
        return nhap

    class Meta:
        verbose_name = 'Danh mục phương tiện'
        verbose_name_plural = 'Danh mục phương tiện'
        ordering = ['chung_loai__maso']

    def __str__(self):
        return self.ten


class Danh_muc_kho(models.Model):
    ten = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Danh mục kho'
        verbose_name_plural = 'Danh mục kho'

    def __str__(self):
        return self.ten


class Danh_muc_nguon_cap(models.Model):
    ten = models.CharField(max_length=200)
    mo_ta = models.CharField(max_length=500, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Danh mục nguồn cấp'
        verbose_name_plural = 'Danh mục nguồn cấp'

    def __str__(self):
        return self.ten


class Phieu_nhap(models.Model):
    thoi_gian = models.DateField(
        verbose_name='Thời gian nhập', null=True, blank=True)
    kho_xuat = models.ForeignKey(
        Danh_muc_kho, verbose_name='Kho xuất', related_name='giao', on_delete=models.RESTRICT, null=True, blank=True)
    kho_nhap = models.ForeignKey(
        Danh_muc_kho, verbose_name='Kho nhập', related_name='nhan', on_delete=models.RESTRICT, default=1)
    nguon_cap = models.ForeignKey(
        Danh_muc_nguon_cap, verbose_name='Nguồn cấp', on_delete=models.RESTRICT, null=True, blank=True)
    note = models.CharField(max_length=500, null=True, blank=True)

    success = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Phiếu nhập'
        verbose_name_plural = 'Phiếu nhập'
        ordering = ['-thoi_gian']

    def __str__(self):
        return self.thoi_gian.strftime("%d/%m/%Y")

    # def printFile(self):
    #     import docx
    #     doc = docx.Document("E:/C20-HD.docx")
    #     print(self.thoi_gian.strftime("%d/%m/%Y"))
    #     doc_replace(doc, "thoi_gian", self.thoi_gian.strftime("%d/%m/%Y"))
    #     doc_replace(doc, "kho_nhap", self.kho_nhap.ten)
    #     table = doc.tables[1]
    #     chitiet = self.chi_tiet_phieu_nhap_set.all()
    #     print(chitiet)
    #     for item in chitiet:
    #         cells = table.add_row().cells
    #         cells[1].text = item.phuong_tien.ten
    #         cells[2].text = str(item.so_luong)
    #         cells[3].text = str(item.nam_cap)
    #         cells[4].text = str(item.nguyen_gia)
    #         insertion_row = table.rows[1]._tr
    #         insertion_row.addnext(table.rows[-1]._tr)
    #     doc.save('E:/out.docx')


class Chi_tiet_phieu_nhap(models.Model):
    phieu_nhap = models.ForeignKey(
        Phieu_nhap, verbose_name='Phiếu nhập', on_delete=models.CASCADE)
    phuong_tien = models.ForeignKey(
        Danh_muc_phuong_tien, verbose_name='Phương tiện', on_delete=models.RESTRICT)
    so_luong = models.IntegerField(verbose_name='Số lượng',)
    from django.core.validators import MaxValueValidator, MinValueValidator
    nam_cap = models.PositiveIntegerField(verbose_name='Năm cấp', validators=[
        MinValueValidator(2000), MaxValueValidator(2022)], null=True, blank=True)
    nguon_cap = models.ForeignKey(
        Danh_muc_nguon_cap, verbose_name='Nguồn cấp', on_delete=models.RESTRICT, null=True, blank=True)
    nguyen_gia = models.PositiveIntegerField(
        verbose_name='Nguyên giá (VNĐ)', null=True, blank=True)

    class Meta:
        verbose_name = 'Chi tiết phiếu nhập'
        verbose_name_plural = 'Chi tiết phiếu nhập'

    def __str__(self):
        return self.phieu_nhap.thoi_gian.strftime('%d/%m/%Y') + ": " + self.phuong_tien.ten

#     def save(self, *args, **kwargs):
#         if not self.id:
#             if not(self.phuong_tien.totals() < self.so_luong):
#                 super(Chi_tiet_phieu_xuat, self).save(*args, **kwargs)
#             else:
#                 raise Exception(
#                     'Không hợp lệ !!! Số lượng xuất lớn hơn số lượng hiện có')
#         else:
#             if not(self.phuong_tien.totals() < (self.so_luong-Chi_tiet_phieu_xuat.objects.get(id=self.id).so_luong)):
#                 super(Chi_tiet_phieu_xuat, self).save(*args, **kwargs)
#             else:
#                 raise Exception(
#                     'Không hợp lệ !!! Số lượng xuất lớn hơn số lượng hiện có')


class Sua_chua(models.Model):
    phuong_tien = models.CharField(max_length=200)
    hu_hong = models.CharField(max_length=500)
    ngay_phat_hien = models.DateField()
    ngay_khac_phuc = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.phuong_tien
