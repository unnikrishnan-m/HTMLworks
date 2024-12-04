# Generated by Django 5.1.1 on 2024-09-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsedVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('owner_type', models.CharField(max_length=200)),
                ('running_kilometers', models.IntegerField()),
                ('price', models.FloatField()),
                ('fuel_type', models.CharField(max_length=200)),
            ],
        ),
    ]