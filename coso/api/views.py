from rest_framework import viewsets
#  For custom allow API
from rest_framework import mixins
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# Import Serializer
from .serializers import DiabanSerializer, CosoSerializer, LoaihinhcosoSerializer, HuanluyenSerializer
# Import Models
from coso.models import Dia_ban, Coso, Loai_hinh_co_so, Huan_luyen
###################################################################################
# Import permissions
from rest_framework import permissions
from api.permissions import IsPostOrAdmin, IsAuthenticatedOrReadOnly
from api.paginations import CustomPagination
from api.decorators import role_required

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.decorators import login_required


class CosoViewSet(viewsets.ModelViewSet):
    queryset = Coso.objects.all()
    serializer_class = CosoSerializer
    pagination_class = CustomPagination
    # permission_classes = [
    #     permissions.IsAuthenticated, IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['dia_ban', 'loai_hinh_co_so',
                        'dang_hoat_dong', 'thuoc_phu_luc_2']
    search_fields = ['ten', 'co_quan_quan_ly']


class DiabanViewSet(viewsets.ModelViewSet):
    queryset = Dia_ban.objects.all()
    serializer_class = DiabanSerializer
    pagination_class = CustomPagination


class LoaihinhcosoViewSet(viewsets.ModelViewSet):
    queryset = Loai_hinh_co_so.objects.all()
    serializer_class = LoaihinhcosoSerializer
    pagination_class = CustomPagination


class HuanluyenViewSet(viewsets.ModelViewSet):
    queryset = Huan_luyen.objects.all()
    serializer_class = HuanluyenSerializer
    pagination_class = CustomPagination
