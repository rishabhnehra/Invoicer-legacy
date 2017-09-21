# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('invoice', models.CharField(max_length=100)),
                ('buyer_name', models.CharField(max_length=50)),
                ('buyer_address', models.CharField(max_length=150)),
                ('buyer_gstin', models.CharField(max_length=15)),
                ('buyer_mobile', models.CharField(max_length=10)),
                ('date_of_issue', models.DateField()),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.CharField(max_length=100)),
                ('item_type', models.CharField(max_length=100)),
                ('hsn', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('rate', models.DecimalField(max_digits=10, decimal_places=2)),
                ('discount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('taxable_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cgst_rate', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cgst_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('sgst_rate', models.DecimalField(max_digits=10, decimal_places=2)),
                ('sgst_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('igst_rate', models.DecimalField(max_digits=10, decimal_places=2)),
                ('igst_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('bill', models.ForeignKey(to='bill.Bill')),
            ],
        ),
    ]
