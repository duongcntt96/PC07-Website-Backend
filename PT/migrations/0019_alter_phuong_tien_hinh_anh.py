# Generated by Django 3.2.4 on 2021-08-27 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PT', '0018_auto_20210821_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phuong_tien',
            name='hinh_anh',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/upload/'),
        ),
    ]
