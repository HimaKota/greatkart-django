# Generated by Django 3.1 on 2022-10-19 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20221019_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='variation_price',
        ),
    ]
