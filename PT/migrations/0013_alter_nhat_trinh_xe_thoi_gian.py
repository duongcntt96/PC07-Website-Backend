# Generated by Django 3.2.4 on 2021-08-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PT', '0012_nhat_trinh_xe_thoi_gian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhat_trinh_xe',
            name='thoi_gian',
            field=models.DateField(null=True),
        ),
    ]
