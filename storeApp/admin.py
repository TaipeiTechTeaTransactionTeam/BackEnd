from django.contrib import admin
from .models import product, store, teaType,SeasoningDiscount,ShippingDiscount,productDiscount
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','teaType','image','amount','price','description','AddDate')
    fields = ('name','teaType','image','amount','price','description')
    ordering = ('AddDate',)

class TeaTypeAdmin(admin.ModelAdmin):
    list_display = ('name','image')

class SeasoningDiscountAdmin(admin.ModelAdmin):
    list_display = ('id','discount','start_date','end_date')

class ShippingDiscountAdmin(admin.ModelAdmin):
    list_display = ('id','discount','condition','start_date','end_date')

class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = ('id','discount','product','start_date','end_date')

admin.site.register(product,ProductAdmin)
admin.site.register(store)
admin.site.register(teaType,TeaTypeAdmin)
admin.site.register(SeasoningDiscount,SeasoningDiscountAdmin)
admin.site.register(ShippingDiscount,ShippingDiscountAdmin)
admin.site.register(productDiscount,ProductDiscountAdmin)
