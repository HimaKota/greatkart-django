# Generated by Django 3.1 on 2022-10-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_variation_variation_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_price',
            field=models.IntegerField(default=True),
        ),
    ]
