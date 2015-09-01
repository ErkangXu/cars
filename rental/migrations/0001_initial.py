# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('car_name', models.CharField(max_length=100)),
                ('make', models.CharField(max_length=50)),
                ('engine_identification', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=50)),
                ('plateName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('birth_day', models.DateField()),
                ('gender', models.CharField(max_length=20, choices=[('M', 'Male'), ('F', 'Female')])),
                ('license_number', models.CharField(max_length=50)),
                ('ID_number', models.CharField(max_length=60)),
                ('hometown', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('total_amount', models.IntegerField()),
                ('security_deposit_return', models.BooleanField()),
                ('payment_type', models.CharField(max_length=10, choices=[('CASH', 'Cash'), ('CARD', 'Card')])),
                ('car', models.ForeignKey(to='rental.Car')),
                ('customer', models.ForeignKey(to='rental.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('location', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('kind', models.CharField(max_length='30')),
                ('fine', models.PositiveIntegerField()),
                ('points', models.PositiveSmallIntegerField()),
                ('note', models.TextField()),
                ('handled', models.BooleanField()),
                ('car', models.ForeignKey(to='rental.Car')),
                ('violator', models.ForeignKey(to='rental.Customer')),
            ],
        ),
    ]
