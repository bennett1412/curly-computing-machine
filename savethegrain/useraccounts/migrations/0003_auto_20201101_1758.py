# Generated by Django 3.1.2 on 2020-11-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0002_auto_20201101_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stguserprofile',
            name='Location',
            field=models.TextField(max_length=60),
        ),
    ]
