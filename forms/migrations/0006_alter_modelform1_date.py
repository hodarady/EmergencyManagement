# Generated by Django 4.0.4 on 2022-06-28 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_modelform1_exitdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelform1',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 5, 52, 39, 273225), verbose_name='Date'),
        ),
    ]
