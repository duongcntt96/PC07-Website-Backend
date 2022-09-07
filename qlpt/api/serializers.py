from qlpt.models import Chung_loai, Danh_muc_kho, Danh_muc_nguon_cap, Danh_muc_phuong_tien, Chi_tiet_phieu_nhap, Phieu_nhap
from rest_framework import serializers


class Danh_muc_phuong_tien_Serializer(serializers.ModelSerializer):
    totals = serializers.IntegerField(read_only=True)

    class Meta:
        model = Danh_muc_phuong_tien
        fields = '__all__'


class phuong_tiens(serializers.ModelSerializer):
    info = Danh_muc_phuong_tien_Serializer(source='phuong_tien')

    class Meta:
        model = Chi_tiet_phieu_nhap
        fields = '__all__'


class Phieu_nhap_Serializer(serializers.ModelSerializer):
    phuong_tiens = phuong_tiens(
        source='chi_tiet_phieu_nhap_set', many=True, read_only=True)
    thoi_gian = serializers.DateField()
    # thoi_gian = serializers.DateField(
    #     format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])

    class Meta:
        model = Phieu_nhap
        fields = '__all__'
        read_only_fields = ['']


class Chi_tiet_phieu_nhap_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Chi_tiet_phieu_nhap
        fields = "__all__"
        # fields = (
        #     "id",
        #     "so_luong",
        #     "phieu_nhap",
        #     "phuong_tien",
        # )


class Danh_muc_kho_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Danh_muc_kho
        fields = "__all__"


class Danh_muc_nguon_cap_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Danh_muc_nguon_cap
        fields = "__all__"


class Chung_loaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chung_loai
        fields = "__all__"
