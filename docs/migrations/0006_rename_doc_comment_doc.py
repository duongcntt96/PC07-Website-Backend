# Generated by Django 3.2.4 on 2022-01-20 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0005_auto_20220120_0939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Doc',
            new_name='doc',
        ),
    ]
