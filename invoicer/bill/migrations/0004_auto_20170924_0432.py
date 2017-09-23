# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0003_auto_20170924_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='place_of_supply',
            field=models.IntegerField(max_length=30, choices=[(1, 'Jammu & Kashmir'), (2, 'Himachal Pradesh'), (3, 'Punjab'), (4, 'Chandigarh'), (5, 'Uttarakhand'), (6, 'Haryana'), (7, 'Delhi'), (8, 'Rajasthan'), (9, 'Uttar Pradesh'), (10, 'Bihar'), (11, 'Sikkim'), (12, 'Arunachal Pradesh'), (13, 'Nagaland'), (14, 'Manipur'), (15, 'Mizoram'), (16, 'Tripura'), (17, 'Meghalaya'), (18, 'Assam'), (19, 'West Bengal'), (20, 'Jharkhand'), (21, 'Odisha'), (22, 'Chhattisgarh'), (23, 'Madhya Pradesh'), (24, 'Gujarat'), (25, 'Daman & Diu'), (26, 'Dadra & Nagar Haveli'), (27, 'Maharashtra'), (29, 'Karnataka'), (30, 'Goa'), (31, 'Lakshdweep'), (32, 'Kerala'), (33, 'Tamil Nadu'), (34, 'Pondicherry'), (35, 'Andaman & Nicobar Island'), (36, 'Telangana'), (37, 'Andhra Pradesh'), (97, 'Other Territory')]),
        ),
    ]
