# Generated by Django 3.1.2 on 2020-11-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stguserprofile',
            name='user_type',
            field=models.CharField(choices=[('DNR', 'Donor'), ('NGO', 'NGO')], max_length=3),
        ),
    ]
