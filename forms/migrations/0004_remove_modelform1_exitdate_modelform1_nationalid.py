# Generated by Django 4.0.4 on 2022-06-27 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_remove_modelform1_diagnosis_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelform1',
            name='exitDate',
        ),
        migrations.AddField(
            model_name='modelform1',
            name='nationalId',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
