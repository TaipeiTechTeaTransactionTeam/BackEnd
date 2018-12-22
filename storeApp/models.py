from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone
from django.urls import reverse
# Create your models here.


class store(models.Model):

    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=10, null=False, unique=True)

    def __str__(self):
        return self.name


class teaType(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='teaType')

    def __str__(self):
        return self.name


class product(models.Model):

    image = models.ImageField(upload_to='product')
    name = models.CharField(max_length=255, null=False, unique=True)
    teaType = models.ForeignKey(teaType, on_delete=models.CASCADE, default="")
    amount = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    description = models.TextField(max_length=255, null=False)
    AddDate = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('storeApp:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class shoppingCart(models.Model):
    ownUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class shoppingCartContainProduct(models.Model):
    shoppingCart = models.ForeignKey(shoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    purchase_quantity = models.PositiveIntegerField()

class order(models.Model):
    ownUser = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=False)
    Date = models.DateField(default=timezone.now)
    Total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.ownUser.name

class OrderContainProduct(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    purchase_quantity = models.PositiveIntegerField()


class SeasoningDiscount(models.Model):
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.discount

class ShippingDiscount(SeasoningDiscount):
    condition = models.DecimalField(max_digits=10, decimal_places=0, null=False)

class productDiscount(SeasoningDiscount):
    product = models.ForeignKey(product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
