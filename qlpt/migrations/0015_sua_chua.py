# Generated by Django 3.2.4 on 2022-07-25 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlpt', '0014_auto_20220607_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sua_chua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phuong_tien', models.CharField(max_length=200)),
                ('hu_hong', models.CharField(max_length=500)),
                ('ngay_phat_hien', models.DateField()),
                ('ngay_khac_phuc', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
