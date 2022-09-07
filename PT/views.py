from django.shortcuts import render
from django.http import HttpResponse
from .models import Phuong_tien, Chung_loai
from .forms import editPhuongTienForm, RegistrationForm
from django.db.models import Count, Sum

import json
from django.http import JsonResponse
from django.core import serializers

##================================== INDEX ===========================================###


def index(request):
    return render(request, 'PT/phuongtien.html')
##================================== BASIC ===========================================###
# show


def info(request, id):
    info = Phuong_tien.objects.get(id=id)
    return render(request, 'PT/phuongtieninfo.html', {'info': info})
# update


def edit(request, id):
    instance = Phuong_tien.objects.get(id=id)
    if request.method == 'POST':
        form = editPhuongTienForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved')
        else:
            return HttpResponse('Thông tin không hợp lệ')
    form = editPhuongTienForm(instance=instance)
    return render(request, 'PT/edit.html', {'form': form})
# create


def add(request, id):
    form = RegistrationForm()
    PT = Phuong_tien.objects.get(id=id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(id)
            return render(request, 'PT/add2.html', {'form': form, 'PT': PT, 'noti': 'success'})
    return render(request, 'PT/add2.html', {'form': form, 'PT': PT})
##================================= EXTENDS =========================================###
# query


def list_ten(request):
    data = Phuong_tien.objects.values('ten').annotate(
        c=Sum('so_luong')).order_by('ten')
    return render(request, 'PT/phuongtien-theoten.html', {'data': data})
# query


def list_chung_loai(request):
    data = Chung_loai.objects.all()
    return render(request, 'PT/phuongtien-theochungloai.html', {'data': data})
# query


def list_to(request):
    data = To.objects.all()
    return render(request, 'PT/phuongtien-theoto.html', {'data': data})
# query


def list_noi_bo_tri(request):
    data = Phuong_tien.objects.values('noi_bo_tri', 'noi_bo_tri__ten').annotate(
        c=Count('so_luong')).order_by('noi_bo_tri')
    return render(request, 'PT/phuongtien-theo-noibotri.html', {'data': data})
# query


def search(request):
    format = request.GET.get('format')

    q = request.GET.get('q')
    info = Phuong_tien.objects.filter(ten__contains=q)

    if (format == 'json'):
        qs_json = serializers.serialize('json', info)
        return HttpResponse(qs_json, content_type='application/json')

    total = 0
    for pt in info:
        total += pt.so_luong
    return render(request, 'PT/search.html', {'info': info, 'q': q, 'total': total})
##===================================================================================###
