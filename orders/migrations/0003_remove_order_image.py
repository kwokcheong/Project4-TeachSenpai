# Generated by Django 2.2.6 on 2020-05-27 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image',
        ),
    ]