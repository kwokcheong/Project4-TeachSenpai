# Generated by Django 2.2.6 on 2020-05-29 20:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200530_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='transactionref',
        ),
    ]
