from django.db import models

# Create your models here.

class store(models.Model):

    name = models.CharField(max_length = 255, null = False)
    address = models.CharField(max_length = 255, null = False)
    phone = models.CharField(max_length = 10, null = False, unique = True)

    def __str__(self):
        return self.name
