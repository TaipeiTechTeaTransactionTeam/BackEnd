from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone
from django.urls import reverse
# Create your models here.


class Store(models.Model):

    name = models.CharField(verbose_name="名稱", max_length=255, null=False)
    address = models.CharField(verbose_name="地址", max_length=255, null=False)
    phone = models.CharField(
        verbose_name="手機", max_length=10, null=False, unique=True)
    freight = models.DecimalField(verbose_name="運費",
                                  max_digits=10, decimal_places=0, null=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商店'
        verbose_name_plural = '商店'


class TeaType(models.Model):
    name = models.CharField(verbose_name="名稱", max_length=255, null=False)
    image = models.ImageField(verbose_name="圖片", upload_to='teaType')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '茶葉類型'
        verbose_name_plural = '茶葉類型'


class Product(models.Model):

    image = models.ImageField(verbose_name="圖片", upload_to='product')
    name = models.CharField(
        verbose_name="名稱", max_length=255, null=False, unique=True)
    tea_type = models.ForeignKey(
        TeaType, verbose_name="茶類", on_delete=models.CASCADE, default="")
    amount = models.DecimalField(
        verbose_name="數量", max_digits=10, decimal_places=0, null=False)
    price = models.DecimalField(
        verbose_name="價錢", max_digits=10, decimal_places=0, null=False)
    description = models.TextField(verbose_name="描述", null=False)
    add_date = models.DateField(verbose_name="新增日期", default=timezone.now)

    def get_absolute_url(self):
        return reverse('storeApp:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '產品'
        verbose_name_plural = '產品'


class Order(models.Model):
    own_user = models.ForeignKey(
        User, verbose_name="持有者", on_delete=models.CASCADE)
    status = models.CharField(
        verbose_name="狀態", max_length=255, null=False, default='unpad')
    date = models.DateField(verbose_name="日期", default=timezone.now)
    total_price = models.DecimalField(verbose_name="總金額",
                                      max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.own_user.username

    class Meta:
        verbose_name = '訂單'
        verbose_name_plural = '訂單'


class OrderContainProduct(models.Model):
    order = models.ForeignKey(Order, verbose_name="訂單",
                              on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, verbose_name="產品", on_delete=models.CASCADE)
    purchase_quantity = models.PositiveIntegerField(verbose_name="數量",)

    class Meta:
        verbose_name = '訂單內容'
        verbose_name_plural = '訂單內容'


class SeasoningDiscount(models.Model):
    discount = models.DecimalField(
        verbose_name="折扣", max_digits=10, decimal_places=2, null=False)
    start_date = models.DateField(verbose_name="開始日期", null=False)
    end_date = models.DateField(verbose_name="結束日期", null=False)
    description = models.CharField(
        verbose_name="描述", max_length=255, null=False)


    class Meta:
        verbose_name = '季節折扣'
        verbose_name_plural = '季節折扣'


class ShippingDiscount(SeasoningDiscount):
    condition = models.DecimalField(
        max_digits=10, decimal_places=0, null=False,default=0)

    class Meta:
        verbose_name = '購物折扣'
        verbose_name_plural = '購物折扣'


class ProductDiscount(SeasoningDiscount):
    product = models.ForeignKey(
        Product, verbose_name="產品", on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.product.name

    class Meta:
        verbose_name = '產品折扣'
        verbose_name_plural = '產品折扣'
