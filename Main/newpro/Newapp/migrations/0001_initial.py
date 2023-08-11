# Generated by Django 4.2.4 on 2023-08-11 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cityname', models.CharField(max_length=200)),
                ('Citycode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Countryname', models.CharField(max_length=200)),
                ('Countrycode', models.IntegerField()),
            ],
        ),
    ]
