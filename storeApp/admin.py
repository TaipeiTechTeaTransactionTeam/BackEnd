from django.contrib import admin
from .models import product
from .models import store
from .models import teaType
from .models import SeasoningDiscount
from .models import ShippingDiscount
from .models import productDiscount


@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'teaType', 'image', 'amount',
                    'price', 'description', 'AddDate')
    fields = ('name', 'teaType', 'image', 'amount', 'price', 'description')
    ordering = ('AddDate',)


@admin.register(product)
class TeaTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(SeasoningDiscount)
class SeasoningDiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount', 'start_date', 'end_date')


@admin.register(ShippingDiscount)
class ShippingDiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount', 'condition', 'start_date', 'end_date')


@admin.register(productDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount', 'product', 'start_date', 'end_date')


admin.site.register(store)
