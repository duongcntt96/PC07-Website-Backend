# Generated by Django 3.2.4 on 2021-07-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PT', '0003_alter_phuong_tien_bien_so'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phuong_tien',
            name='thoi_gian_san_xuat',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
