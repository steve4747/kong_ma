# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order_all',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order_main',
            fields=[
                ('order_id', models.CharField(verbose_name='訂單編號', primary_key=True, max_length=64, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ordering', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Price_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tp', models.CharField(max_length=5)),
                ('num', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('prod_nam', models.CharField(max_length=30)),
                ('pord_id', models.ForeignKey(related_name='product_names', to='APP_orderMV.Price_table')),
            ],
        ),
        migrations.AddField(
            model_name='order_all',
            name='order_id',
            field=models.ForeignKey(related_name='Order_ID', to='APP_orderMV.Order_main'),
        ),
    ]
