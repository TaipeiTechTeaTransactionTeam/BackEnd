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

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"


@admin.register(TeaType)
class TeaTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    actions = [make_published]

@admin.register(SeasoningDiscount)
class SeasoningDiscountAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id', 'discount', 'start_date', 'end_date')


@admin.register(ShippingDiscount)
class ShippingDiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount', 'condition', 'start_date', 'end_date')


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount', 'product', 'start_date', 'end_date')


class OrderContainProductInline(admin.TabularInline):
    model = OrderContainProduct
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'own_user']
    inlines = [OrderContainProductInline]


admin.site.register(Store)
