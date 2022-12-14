# Generated by Django 3.2.4 on 2021-07-04 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_luong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_luong', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chung_loai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=200, null=True)),
                ('mo_ta', models.CharField(blank=True, max_length=500, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='PT.chung_loai')),
            ],
        ),
        migrations.CreateModel(
            name='To',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trang_thai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trang_thai', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phuong_tien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=200)),
                ('don_vi_tinh', models.CharField(blank=True, max_length=50, null=True)),
                ('so_luong', models.IntegerField(blank=True, null=True)),
                ('nhan_hieu', models.CharField(blank=True, max_length=200, null=True)),
                ('so_khung', models.CharField(blank=True, max_length=20, null=True)),
                ('so_may', models.CharField(blank=True, max_length=20, null=True)),
                ('nguon_cap', models.CharField(blank=True, max_length=50, null=True)),
                ('thoi_gian_nhan', models.DateField(blank=True, null=True)),
                ('thoi_gian_san_xuat', models.DateField(blank=True, null=True)),
                ('thoi_gian_dua_vao_hoat_dong', models.DateField(blank=True, null=True)),
                ('hinh_anh', models.ImageField(blank=True, null=True, upload_to='static/images/upload/')),
                ('chat_luong', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.RESTRICT, to='PT.chat_luong')),
                ('chung_loai', models.ForeignKey(default=5, on_delete=django.db.models.deletion.RESTRICT, to='PT.chung_loai')),
                ('nguoi_quan_ly', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='PT.to')),
                ('noi_bo_tri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='PT.phuong_tien')),
                ('trang_thai', models.ForeignKey(blank=True, default=5, null=True, on_delete=django.db.models.deletion.RESTRICT, to='PT.trang_thai')),
            ],
        ),
    ]
