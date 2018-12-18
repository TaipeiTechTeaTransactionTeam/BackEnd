from django.contrib import admin
from .models import product, store, teaType
# Register your models here.

admin.site.register(product)
admin.site.register(store)
admin.site.register(teaType)
