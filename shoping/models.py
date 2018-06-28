# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#用户
class User(AbstractUser):
    address = models.CharField(max_length=200, verbose_name='地址')
    phone = models.CharField(max_length=20, verbose_name='联系电话')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username



#广告
class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    index = models.IntegerField(default=1,verbose_name='排列顺序')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index','id']

    def __str__(self):
        return self.title


#分类
class Category(models.Model):
    typ = models.CharField(max_length=20, choices=(('客厅','客厅'),('卧室','卧室'),('餐厅/房','餐厅/书房'),('成套','成套')), verbose_name='大类')
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=1,verbose_name='分类的排序')
    west_east = models.IntegerField(default=0, choices=((0, '中式'),('1','西式')), verbose_name='风格')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index','id']

    def __str__(self):
        return self.name + "---" + self.typ


#品牌
class Brand(models.Model):
    name = models.CharField(max_length=30, verbose_name='品牌名称')
    index = models.IntegerField(default=1, verbose_name='排列顺序')

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name
        ordering = ['index',]

        # def __repr__(self):
        #     return '<Brand  %s>' % self.name

    def __str__(self):
            return self.name

        # def __unicode__(self):
        #     return self.name


#尺寸
class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name='尺寸')
    index = models.IntegerField(default=1, verbose_name='排列顺序')

    class Meta:
        verbose_name = '尺寸'
        verbose_name_plural = verbose_name
        ordering = ['index']

    def __str__(self):
            return self.name


#标签
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#家具
class Furniture(models.Model):
    category = models.ForeignKey(Category, verbose_name='分类')
    name = models.CharField(max_length=30, verbose_name='名称')
    brand = models.ForeignKey(Brand, verbose_name='品牌')
    size = models.ManyToManyField(Size, verbose_name='尺寸')
    old_price = models.FloatField(default=0.0, verbose_name='原价')
    new_price = models.FloatField(default=0.0, verbose_name='现价')
    discount = models.FloatField(default=1, verbose_name='折扣')
    desc = models.CharField(max_length=100, verbose_name='简介')
    sales = models.IntegerField(default=0, verbose_name='销量')
    tag = models.ManyToManyField(Tag, verbose_name='商品风格标签')
    num = models.IntegerField(default=0, verbose_name='库存')
    image_url_i = models.ImageField(upload_to='furniture/%Y/%m', default='furniture/default.jpg', verbose_name='展示图片路径')
    image_url_l = models.ImageField(upload_to='furniture/%Y/%m', default='furniture/default.jpg', verbose_name='详情图片路径1')
    image_url_m = models.ImageField(upload_to='furniture/%Y/%m', default='furniture/default.jpg', verbose_name='详情图片路径2')
    image_url_r = models.ImageField(upload_to='furniture/%Y/%m', default='furniture/default.jpg', verbose_name='详情图片路径3')
    image_url_c = models.ImageField(upload_to='furniture/%Y/%m', default='furniture/ce.jpg', verbose_name='购物车展示图片')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.brand.name + self.category.name + self.name


#购物车条目
# class Caritem(models.Model):
#     furniture = models.ForeignKey(Furniture, verbose_name='购物车产品条目')
#     quantity = models.IntegerField(default=0, verbose_name='数量')
#     sum_price = models.FloatField(default=0.0, verbose_name='小计')
#
#     class Meta:
#         verbose_name = '购物车条目'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return str(self.id)



#购物车
class Car(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')
    goods = models.ForeignKey(Furniture, verbose_name='商品')
    count = models.IntegerField(default=0, verbose_name='数量')
    sum_price = models.FloatField(default=0, verbose_name='小计')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    #计算此商品总价格
    def sum_pri(self):
        self.sum_price = self.goods.new_price*self.count
        return self.sum_price



#订单
class OrderInfo(models.Model):
    ord_user = models.ForeignKey(User, verbose_name='订单用户' )
    odate = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    oIsPay = models.BooleanField(default=False, verbose_name='是否支付')
    ostate = models.CharField(max_length=10, choices=(('已发货','已发货'),('未发货','未发货'),('未付款','未付款')), verbose_name='订单状态')
    staff = models.CharField(max_length=100, verbose_name='')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.ord_user.name+self.ostate)


#订单明细
class Order_list(models.Model):
    furniture = models.ForeignKey(Furniture, verbose_name='商品')
    order = models.ForeignKey(OrderInfo, verbose_name='所属订单')
    price = models.DecimalField(max_length=5, max_digits=5, decimal_places=2, verbose_name='总价格')
    count = models.IntegerField(default=0, verbose_name='数量')

    class Meta:
        verbose_name = '订单明细'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.furniture.name


#评论
class Comment(models.Model):
    comm = models.CharField(max_length=50, verbose_name='评论内容')
    fur_id = models.IntegerField(default=1, verbose_name='商品ID')
    user_id = models.IntegerField(default=1, verbose_name='用户ID')
    order_id = models.IntegerField(default=1, verbose_name='订单ID')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comm

