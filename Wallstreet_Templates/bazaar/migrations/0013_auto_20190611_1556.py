# Generated by Django 2.1.2 on 2019-06-11 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0012_buytable_companytemp1_selltable_companytemp1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buytable_companytemp1',
            name='company',
        ),
        migrations.RemoveField(
            model_name='buytable_companytemp1',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='selltable_companytemp1',
            name='company',
        ),
        migrations.RemoveField(
            model_name='selltable_companytemp1',
            name='proile',
        ),
        migrations.DeleteModel(
            name='BuyTable_CompanyTemp1',
        ),
        migrations.DeleteModel(
            name='SellTable_CompanyTemp1',
        ),
    ]
