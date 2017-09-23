# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bill', '0002_auto_20170922_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('company', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('gstin', models.CharField(max_length=15)),
                ('place_of_supply', models.IntegerField(choices=[(1, 'Jammu & Kashmir'), (2, 'Himachal Pradesh'), (3, 'Punjab'), (4, 'Chandigarh'), (5, 'Uttarakhand'), (6, 'Haryana'), (7, 'Delhi'), (8, 'Rajasthan'), (9, 'Uttar Pradesh'), (10, 'Bihar'), (11, 'Sikkim'), (12, 'Arunachal Pradesh'), (13, 'Nagaland'), (14, 'Manipur'), (15, 'Mizoram'), (16, 'Tripura'), (17, 'Meghalaya'), (18, 'Assam'), (19, 'West Bengal'), (20, 'Jharkhand'), (21, 'Odisha'), (22, 'Chhattisgarh'), (23, 'Madhya Pradesh'), (24, 'Gujarat'), (25, 'Daman & Diu'), (26, 'Dadra & Nagar Haveli'), (27, 'Maharashtra'), (29, 'Karnataka'), (30, 'Goa'), (31, 'Lakshdweep'), (32, 'Kerala'), (33, 'Tamil Nadu'), (34, 'Pondicherry'), (35, 'Andaman & Nicobar Island'), (36, 'Telangana'), (37, 'Andhra Pradesh'), (97, 'Other Territory')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='bill',
            name='buyer_address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='bill',
            name='buyer_gstin',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='bill',
            name='buyer_mobile',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='bill',
            name='buyer_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bill',
            name='invoice',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='cgst_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='cgst_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='hsn',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='igst_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='igst_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='sgst_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='sgst_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='taxable_value',
            field=models.FloatField(),
        ),
    ]
