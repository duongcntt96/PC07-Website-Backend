# Generated by Django 3.2.4 on 2021-08-01 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PT', '0007_phuong_tien_so_dong_co'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinh_muc_nhien_lieu',
            fields=[
                ('phuong_tien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='PT.phuong_tien')),
                ('dinh_muc_1', models.FloatField(blank=True, null=True)),
                ('dinh_muc_2', models.FloatField(blank=True, null=True)),
                ('dinh_muc_3', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
