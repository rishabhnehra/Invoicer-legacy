# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='buyer_address',
            field=models.CharField(max_length=150, default='N/A'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='buyer_gstin',
            field=models.CharField(max_length=15, default='N/A'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='buyer_mobile',
            field=models.CharField(max_length=10, default='N/A'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='buyer_name',
            field=models.CharField(max_length=50, default='N/A'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='invoice',
            field=models.CharField(max_length=100, default='dummy'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='cgst_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='cgst_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100, default='N/A'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='hsn',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='igst_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='igst_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_type',
            field=models.CharField(max_length=100, default='N/A'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='sgst_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='sgst_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='taxable_value',
            field=models.FloatField(default=0),
        ),
    ]
