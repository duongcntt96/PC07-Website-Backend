# Generated by Django 3.2.4 on 2022-06-07 10:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlpt', '0013_auto_20220607_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chi_tiet_phieu_nhap',
            name='nam_cap',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2022)], verbose_name='Năm cấp'),
        ),
        migrations.AlterField(
            model_name='phieu_nhap',
            name='thoi_gian',
            field=models.DateField(blank=True, null=True, verbose_name='Thời gian nhập'),
        ),
    ]
