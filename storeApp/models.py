from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

# Create your models here.

class store(models.Model):

    name = models.CharField(max_length = 255, null = False)
    address = models.CharField(max_length = 255, null = False)
    phone = models.CharField(max_length = 10, null = False, unique = True)

    def __str__(self):
        return self.name

class product(models.Model):
    image = models.CharField(max_length = 255, null = False,default="")
    name = models.CharField(max_length = 255, null = False, unique = True)
    amount = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    description = models.TextField(max_length=255, null=False)
    
    def __str__(self):
        return self.name

class shoppingCart(models.Model):
    ownUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class shoppingCartContainProduct(models.Model):
    shoppingCart = models.ForeignKey(shoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    purchase_quantity = models.PositiveIntegerField()

class order(models.Model):
    ownUser = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null = False)
    Date = models.DateField(default = timezone.now)
    Total_price = models.DecimalField(max_digits=10, decimal_places=2, null = False)

    def __str__(self):
        return self.ownUser.name

class discount(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, null = False)
    type = models.CharField(max_length=25, null = False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    def __str__(self):
        return self.type

class productDiscount(discount):
    product = models.ForeignKey(product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name