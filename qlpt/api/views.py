from datetime import datetime
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
#  For custom allow API
from rest_framework import mixins

from qlpt.utils import text_to_mp3

# Import Serializer
from .serializers import Chung_loaiSerializer, Danh_muc_kho_Serializer, Danh_muc_nguon_cap_Serializer, Danh_muc_phuong_tien_Serializer, Chi_tiet_phieu_nhap_Serializer, Phieu_nhap_Serializer
# Import Models
from rest_framework import permissions
from api.permissions import IsPostOrAdmin, IsAuthenticatedOrReadOnly, ObjectPermission
from api.paginations import CustomPagination
from rest_framework.response import Response
from rest_framework import status

from qlpt.models import Danh_muc_kho, Danh_muc_nguon_cap, Danh_muc_phuong_tien, Chi_tiet_phieu_nhap, Phieu_nhap, Chung_loai


class Text_to_speak(APIView):
    def get(self, request):
        text = request.query_params.get('text')
        return Response({'data': text_to_mp3(text)})


class Danh_muc_kho_viewSet(viewsets.ModelViewSet):
    queryset = Danh_muc_kho.objects.all()
    serializer_class = Danh_muc_kho_Serializer


class Danh_muc_nguon_cap_viewSet(viewsets.ModelViewSet):
    queryset = Danh_muc_nguon_cap.objects.all()
    serializer_class = Danh_muc_nguon_cap_Serializer


class Chung_loai_viewSet(viewsets.ModelViewSet):
    queryset = Chung_loai.objects.all()
    serializer_class = Chung_loaiSerializer


class Danh_muc_phuong_tien_ViewSet(viewsets.ModelViewSet):
    queryset = Danh_muc_phuong_tien.objects.all()
    serializer_class = Danh_muc_phuong_tien_Serializer
    filterset_fields = ['kho_nhap', 'chung_loai']

    def list(self, request):
        # Default list
        if (request.query_params.get('to_import')):
            queryset = Danh_muc_phuong_tien.objects.all()
            serializer = Danh_muc_phuong_tien_Serializer(queryset, many=True)
            return Response({'data': serializer.data})

        print("Listing")
    #    Phieu_nhap.objects.get(id=11).printFile()

        # Custom list
        kho_nhap = request.query_params.get('kho_nhap')
        chung_loai = request.query_params.get('chung_loai')
        success = True
        if request.query_params.get('success') == "false":
            success = False
        kho_is_active = True
        if kho_nhap:
            kho_is_active = Danh_muc_kho.objects.get(id=kho_nhap).active
        # Get queryset
        phuong_tien_nhap = Chi_tiet_phieu_nhap.objects.filter(
            phieu_nhap__success=success, phieu_nhap__kho_nhap__active=kho_is_active, phieu_nhap__kho_nhap__isnull=False)

        phuong_tien_xuat = Chi_tiet_phieu_nhap.objects.filter(
            phieu_nhap__success=success, phieu_nhap__kho_xuat__isnull=False)

        # Filter object

        if not (kho_nhap == None or kho_nhap == ""):
            phuong_tien_nhap = phuong_tien_nhap.filter(
                phieu_nhap__kho_nhap=kho_nhap)
            phuong_tien_xuat = phuong_tien_xuat.filter(
                phieu_nhap__kho_xuat=kho_nhap)
        if not (chung_loai == None or chung_loai == ""):
            phuong_tien_nhap = phuong_tien_nhap.filter(
                phuong_tien__chung_loai__maso__icontains=Chung_loai.objects.get(id=chung_loai).maso)
            phuong_tien_xuat = phuong_tien_xuat.filter(
                phuong_tien__chung_loai__maso__icontains=Chung_loai.objects.get(id=chung_loai).maso)
        # Annotate totals
        from django.db.models import Sum
        phuong_tien_nhap = phuong_tien_nhap.values('phuong_tien', 'phuong_tien__chung_loai', 'phuong_tien__ten').annotate(
            totals=Sum('so_luong'))
        phuong_tien_xuat = phuong_tien_xuat.values('phuong_tien', 'phuong_tien__chung_loai', 'phuong_tien__ten').annotate(
            totals=Sum('so_luong'))
        # Nhập - Xuất
        for pt in phuong_tien_nhap:
            _xuat = phuong_tien_xuat.filter(phuong_tien=pt['phuong_tien'])
            if _xuat:
                pt['totals'] = pt['totals']-_xuat[0]['totals']

        for pt in phuong_tien_nhap:
            pt['id'] = pt['phuong_tien']
            pt['ten'] = pt['phuong_tien__ten']
            pt['chung_loai'] = pt['phuong_tien__chung_loai']
            del pt['phuong_tien']
            del pt['phuong_tien__ten']
            del pt['phuong_tien__chung_loai']

        # pt = Danh_muc_phuong_tien.objects.filter(totals=0)

        return Response({'data': list(phuong_tien_nhap)}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = Danh_muc_phuong_tien_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Post saved !'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not found', }, status=status.HTTP_404_NOT_FOUND)


class Phieu_nhap_ViewSet(viewsets.ModelViewSet):
    serializer_class = Phieu_nhap_Serializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['kho_nhap', 'kho_xuat', 'thoi_gian', 'nguon_cap', 'success',
                        'chi_tiet_phieu_nhap__phuong_tien', 'chi_tiet_phieu_nhap__nguon_cap']
    search_fields = ["ten", "chung_loai__ten"]
    # def queryset(self):
    # return Phieu_nhap.objects.all()
    # self.request.query_params.get('kho_nhap')
    queryset = Phieu_nhap.objects.all()

    def get_queryset(self):
        start = self.request.query_params.get('thoi_gian__start')
        end = self.request.query_params.get('thoi_gian__end')
        if (start == None or start == ''):
            start = '2000-01-01'
        if (end == None or end == ''):
            end = datetime.now().date()
        queryset = Phieu_nhap.objects.filter(
            thoi_gian__gte=start, thoi_gian__lte=end)
        return queryset


class Chi_tiet_phieu_nhap_ViewSet(viewsets.ModelViewSet):
    # List phiếu nhập có trạng thái success
    queryset = Chi_tiet_phieu_nhap.objects.filter(
        phieu_nhap__success=True)
    serializer_class = Chi_tiet_phieu_nhap_Serializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['phieu_nhap', 'phuong_tien',
                        'phieu_nhap__success', 'phieu_nhap__kho_nhap', 'phieu_nhap__nguon_cap']
