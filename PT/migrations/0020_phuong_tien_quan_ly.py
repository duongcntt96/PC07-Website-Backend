# Generated by Django 3.2.4 on 2022-01-10 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20211003_1037'),
        ('PT', '0019_alter_phuong_tien_hinh_anh'),
    ]

    operations = [
        migrations.AddField(
            model_name='phuong_tien',
            name='quan_ly',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='profiles.team'),
        ),
    ]
