# Generated by Django 4.0.4 on 2022-06-27 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelForm1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('drdep', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('roomNumber', models.IntegerField()),
                ('Diagnosis', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('phonenumber', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'ذكر'), ('F', 'أنثى')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ModelForm2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('drdep', models.CharField(default='وحدة الاستاذ الدكتور', max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('roomNumber', models.IntegerField()),
                ('Diagnosis', models.CharField(max_length=100)),
            ],
        ),
    ]
