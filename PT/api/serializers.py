from PT.models import Chat_luong, Image, Phuong_tien, Chung_loai, Dinh_muc_nhien_lieu, Nhat_trinh_xe, Trang_thai
from rest_framework import serializers

from profiles.models import Team


class PhuongtienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phuong_tien
        # fields = '__all__'
        fields = (
            "hinh_anh",
            "id",
            "ten",
            "don_vi_tinh",
            "so_luong",
            "nhan_hieu",
            "so_khung",
            "so_may",
            "so_dong_co",
            "bien_so",
            "nguon_cap",
            "thoi_gian_nhan",
            "thoi_gian_san_xuat",
            "thoi_gian_dua_vao_hoat_dong",
            "order",
            "chung_loai",
            'chung_loai__ten',

            "trang_thai",
            "trang_thai__ten",

            "chat_luong",
            "chat_luong__ten",

            "noi_bo_tri",
            "noi_bo_tri__ten",

            "quan_ly",
            "quan_ly__name",

        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TrangthaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trang_thai
        fields = '__all__'


class ChatluongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat_luong
        fields = '__all__'


class ChungloaiSerializer(serializers.ModelSerializer):
    # phuongtien_list = PhuongtienSerializer(many=True)
    class Meta:
        model = Chung_loai
        fields = ['id', 'ten']


class DinhmucnhienlieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinh_muc_nhien_lieu
        fields = '__all__'


class NhattrinhxeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nhat_trinh_xe
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
