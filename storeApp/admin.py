from django.contrib import admin
from .models import Product
from .models import Store
from .models import TeaType
from .models import Order, OrderContainProduct
from .models import SeasoningDiscount
from .models import ShippingDiscount
from .models import ProductDiscount


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'tea_type', 'image', 'amount',
                    'price', 'description', 'add_date')
    fields = ('name', 'tea_type', 'image', 'amount', 'price', 'description')
    ordering = ('add_date',)


@admin.register(TeaType)
class TeaTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


@admin.register(SeasoningDiscount)
class SeasoningDiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount', 'start_date', 'end_date')


@admin.register(ShippingDiscount)
class ShippingDiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount', 'condition', 'start_date', 'end_date')


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount', 'product', 'start_date', 'end_date')


class OrderContainProductInline(admin.TabularInline):
    model = OrderContainProduct
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderContainProductInline]


admin.site.register(Store)
