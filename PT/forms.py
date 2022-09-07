from django import forms
import re
from django.contrib.auth.models import User

from .models import Phuong_tien, Chung_loai, Trang_thai, Chat_luong


class editPhuongTienForm(forms.ModelForm):
    class Meta:
        model = Phuong_tien
        fields = '__all__'
        widgets = {
            'ten': forms.TextInput(attrs={'placeholder': 'Vòi chữa cháy', 'class': 'form-control'}),
            'chung_loai': forms.Select(attrs={'class': 'form-control'}),
            'don_vi_tinh': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cuộn', 'value': 'Chiếc'}),
            'so_luong': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10'}),
            'trang_thai': forms.Select(attrs={'class': 'form-control', 'selected': 5}),
            'noi_bo_tri': forms.Select(attrs={'class': 'form-control', 'selected': 5}),
            'nguoi_quan_ly': forms.Select(attrs={'class': 'form-control', 'selected': 5}),
            'chat_luong': forms.Select(attrs={'class': 'form-control'}),
            'nhan_hieu': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10'}),
            'so_khung': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10'}),
            'so_may': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10'}),
            'so_dong_co': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10'}),
            'bien_so': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10'}),
            'quan_ly': forms.Select(attrs={'class': 'form-control'}),
            'nguon_cap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'C07/CAT/UBT/...'}),
            'thoi_gian_nhan': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control', 'placeholder': '09/02/1996'}),
            'thoi_gian_san_xuat': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control', 'placeholder': '09/02/1996'}),
            'thoi_gian_dua_vao_hoat_dong': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control', 'placeholder': '09/02/1996'}),
            'hinh_anh': forms.FileInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        instance = super(editPhuongTienForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance


class RegistrationForm(forms.Form):
    ten = forms.CharField(label='Tên phương tiện', max_length=200,
                          widget=forms.TextInput(attrs={'placeholder': 'Vòi chữa cháy', 'class': 'form-control'}))
    chung_loai = forms.ModelChoiceField(queryset=Chung_loai.objects.all(), label='Chủng loại',
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    don_vi_tinh = forms.CharField(label='Đơn vị tính', max_length=50,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cuộn', 'value': 'Chiếc'}))
    so_luong = forms.IntegerField(label='Số lượng',
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10'}))
    trang_thai = forms.ModelChoiceField(queryset=Trang_thai.objects.all(), label='Trạng thái', initial=3,
                                        widget=forms.Select(attrs={'class': 'form-control', 'selected': 5}))
    chat_luong = forms.ModelChoiceField(queryset=Chat_luong.objects.all(), label="Chất lượng",
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    # quan_ly = forms.ModelChoiceField(queryset=To.objects.all(), label="Quản lý",
    #     widget=forms.Select(attrs={'class':'form-control'}))
    # nguon_cap = forms.CharField(label="Nguồn cấp",max_length=200,
    #     widget=forms.TextInput(attrs={'class':'form-control','placeholder':'C07/CAT/UBT/...'}))
    # nguon_cap = forms.FileField(label="File nguồn cấp",
    #     widget=forms.FileInput(attrs={'class':'custom-file-input'}))
    # thoi_gian_nhan = forms.DateField(label="Thời gian nhận",
    #     widget=forms.DateInput(format=('%d/%m/%Y'),attrs={'class':'form-control','placeholder':'09/02/1996'}))
    # thoi_gian_nhan = models.DateField(null=True, blank=True)
    # thoi_gian_san_xuat = models.DateField(null=True, blank=True)
    # thoi_gian_dua_vao_hoat_dong = models.DateField(null=True, blank=True)
    # hinh_anh = models.ImageField(upload_to='static/images/upload/', null=True, blank=True)

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self, id):
        info = Phuong_tien()
        info.noi_bo_tri = Phuong_tien.objects.get(id=id)
        info.nguoi_quan_ly = info.noi_bo_tri.nguoi_quan_ly
        info.ten = self.cleaned_data['ten']
        info.chung_loai = self.cleaned_data['chung_loai']
        info.don_vi_tinh = self.cleaned_data['don_vi_tinh']
        info.so_luong = self.cleaned_data['so_luong']
        info.trang_thai = self.cleaned_data['trang_thai']
        info.chat_luong = self.cleaned_data['chat_luong']
        info.save()
