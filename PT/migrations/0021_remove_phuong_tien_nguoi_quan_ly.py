# Generated by Django 3.2.4 on 2022-01-10 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PT', '0020_phuong_tien_quan_ly'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phuong_tien',
            name='nguoi_quan_ly',
        ),
    ]
