# Generated by Django 3.1 on 2022-10-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userprofile_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='pincode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
