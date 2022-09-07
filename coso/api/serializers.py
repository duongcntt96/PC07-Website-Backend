from rest_framework import serializers
from coso.models import Dia_ban, Coso, Loai_hinh_co_so, Huan_luyen


class DiabanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dia_ban
        fields = '__all__'


class CosoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coso
        fields = ('id',
                  'ten',
                  'dia_chi',
                  'sdt',
                  'co_quan_quan_ly',
                  'sdt_co_quan_quan_ly',
                  'nganh_nghe',
                  'thuoc_phu_luc_2',
                  'dang_hoat_dong',
                  'dia_ban',
                  'loai_hinh_co_so',
                  'diaban',
                  'loaihinhcoso', )


class LoaihinhcosoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loai_hinh_co_so
        fields = '__all__'


class HuanluyenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huan_luyen
        fields = '__all__'
