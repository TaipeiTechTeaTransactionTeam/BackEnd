from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone
from django.urls import reverse
# Create your models here.


class Store(models.Model):

    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=10, null=False, unique=True)
    freight = models.DecimalField(
        max_digits=10, decimal_places=0, null=False, default=0)

    def __str__(self):
        return self.name


class TeaType(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='teaType')

    def __str__(self):
        return self.name


class Product(models.Model):

    image = models.ImageField(upload_to='product')
    name = models.CharField(max_length=255, null=False, unique=True)
    tea_type = models.ForeignKey(TeaType, on_delete=models.CASCADE, default="")
    amount = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    description = models.TextField(null=False)
    add_date = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('storeApp:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Order(models.Model):
    own_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=False, default='unpad')
    date = models.DateField(default=timezone.now)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.own_user.username


class OrderContainProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_quantity = models.PositiveIntegerField()


class SeasoningDiscount(models.Model):
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.discount


class ShippingDiscount(SeasoningDiscount):
    condition = models.DecimalField(
        max_digits=10, decimal_places=0, null=False)


class ProductDiscount(SeasoningDiscount):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
