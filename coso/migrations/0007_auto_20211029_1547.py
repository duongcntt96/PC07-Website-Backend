# Generated by Django 3.2.4 on 2021-10-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coso', '0006_auto_20211029_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coso',
            name='trang_thai',
        ),
        migrations.AddField(
            model_name='coso',
            name='dang_hoat_dong',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Trang_thai',
        ),
    ]
