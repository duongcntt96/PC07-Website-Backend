# Generated by Django 3.2.4 on 2021-10-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coso', '0003_alter_coso_nganh_nghe'),
    ]

    operations = [
        migrations.AddField(
            model_name='coso',
            name='thuoc_phu_luc_2',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
