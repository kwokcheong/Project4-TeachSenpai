# Generated by Django 2.2.6 on 2020-05-30 22:00

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
