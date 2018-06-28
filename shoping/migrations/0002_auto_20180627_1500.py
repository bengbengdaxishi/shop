# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shoping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='品牌名称', max_length=30)),
                ('index', models.IntegerField(verbose_name='排列顺序', default=1)),
            ],
            options={
                'verbose_name': '品牌',
                'verbose_name_plural': '品牌',
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('count', models.IntegerField(verbose_name='数量', default=0)),
                ('sum_price', models.FloatField(verbose_name='小计', default=0)),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('comm', models.CharField(verbose_name='评论内容', max_length=50)),
                ('fur_id', models.IntegerField(verbose_name='商品ID', default=1)),
                ('user_id', models.IntegerField(verbose_name='用户ID', default=1)),
                ('order_id', models.IntegerField(verbose_name='订单ID', default=1)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='名称', max_length=30)),
                ('old_price', models.FloatField(verbose_name='原价', default=0.0)),
                ('new_price', models.FloatField(verbose_name='现价', default=0.0)),
                ('discount', models.FloatField(verbose_name='折扣', default=1)),
                ('desc', models.CharField(verbose_name='简介', max_length=100)),
                ('sales', models.IntegerField(verbose_name='销量', default=0)),
                ('num', models.IntegerField(verbose_name='库存', default=0)),
                ('image_url_i', models.ImageField(verbose_name='展示图片路径', default='furniture/default.jpg', upload_to='furniture/%Y/%m')),
                ('image_url_l', models.ImageField(verbose_name='详情图片路径1', default='furniture/default.jpg', upload_to='furniture/%Y/%m')),
                ('image_url_m', models.ImageField(verbose_name='详情图片路径2', default='furniture/default.jpg', upload_to='furniture/%Y/%m')),
                ('image_url_r', models.ImageField(verbose_name='详情图片路径3', default='furniture/default.jpg', upload_to='furniture/%Y/%m')),
                ('image_url_c', models.ImageField(verbose_name='购物车展示图片', default='furniture/ce.jpg', upload_to='furniture/%Y/%m')),
                ('brand', models.ForeignKey(verbose_name='品牌', to='shoping.Brand')),
                ('category', models.ForeignKey(verbose_name='分类', to='shoping.Category')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Order_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(verbose_name='总价格', max_length=5, max_digits=5, decimal_places=2)),
                ('count', models.IntegerField(verbose_name='数量', default=0)),
                ('furniture', models.ForeignKey(verbose_name='商品', to='shoping.Furniture')),
            ],
            options={
                'verbose_name': '订单明细',
                'verbose_name_plural': '订单明细',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('odate', models.DateTimeField(verbose_name='创建时间', auto_now=True)),
                ('oIsPay', models.BooleanField(verbose_name='是否支付', default=False)),
                ('ostate', models.CharField(verbose_name='订单状态', max_length=10, choices=[('已发货', '已发货'), ('未发货', '未发货'), ('未付款', '未付款')])),
                ('staff', models.CharField(verbose_name='', max_length=100)),
                ('ord_user', models.ForeignKey(verbose_name='订单用户', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='尺寸', max_length=20)),
                ('index', models.IntegerField(verbose_name='排列顺序', default=1)),
            ],
            options={
                'verbose_name': '尺寸',
                'verbose_name_plural': '尺寸',
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='标签', max_length=30)),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.AddField(
            model_name='order_list',
            name='order',
            field=models.ForeignKey(verbose_name='所属订单', to='shoping.OrderInfo'),
        ),
        migrations.AddField(
            model_name='furniture',
            name='size',
            field=models.ManyToManyField(verbose_name='尺寸', to='shoping.Size'),
        ),
        migrations.AddField(
            model_name='furniture',
            name='tag',
            field=models.ManyToManyField(verbose_name='商品风格标签', to='shoping.Tag'),
        ),
        migrations.AddField(
            model_name='car',
            name='goods',
            field=models.ForeignKey(verbose_name='商品', to='shoping.Furniture'),
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(verbose_name='用户', to=settings.AUTH_USER_MODEL),
        ),
    ]
