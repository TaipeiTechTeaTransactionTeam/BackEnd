from django.contrib import admin
from .models import product, store, teaType
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','teaType','image','amount','price','description','AddDate')
    fields = ('name','teaType','image','amount','price','description')
    ordering = ('AddDate',)

class TeaTypeAdmin(admin.ModelAdmin):
    list_display = ('name','image')

admin.site.register(product,ProductAdmin)
admin.site.register(store)
admin.site.register(teaType,TeaTypeAdmin)
