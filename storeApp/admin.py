from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.db.models import Sum
from .models import Product
from .models import Store
from .models import TeaType
from .models import Order, OrderContainProduct
from .models import SeasoningDiscount
from .models import ShippingDiscount
from .models import ProductDiscount
from .models import ProductReport
from .models import OrderReport


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'tea_type', 'amount',
                    'price', 'description', 'image', 'add_date']
    fields = ['name', 'tea_type', 'image', 'amount', 'price', 'description']
    ordering = ['add_date', ]


@admin.register(TeaType)
class TeaTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


@admin.register(SeasoningDiscount)
class SeasoningDiscountAdmin(admin.ModelAdmin):
    list_display = ['description', 'discount', 'id', 'start_date', 'end_date']


@admin.register(ShippingDiscount)
class ShippingDiscountAdmin(admin.ModelAdmin):
    list_display = ['description', 'id', 'discount',
                    'condition', 'start_date', 'end_date']


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = ['description', 'id', 'discount',
                    'product', 'start_date', 'end_date']


class OrderContainProductInline(admin.TabularInline):
    model = OrderContainProduct
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'own_user', 'status', 'date', 'total_price']
    inlines = [OrderContainProductInline]

@admin.register(ProductReport)
class ProductReportAdmin(admin.ModelAdmin):
    change_list_template = 'storeApp/adminProductReport.html'
    date_hierarchy = 'order__date' # 通过日期过滤对象

    def changelist_view(self, request, extra_context={}):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total_sales': Sum('purchase_quantity'),
        }

        response.context_data['summary'] = list(
            qs
            .filter(order__status='3')
            .values('product__name')
            .annotate(**metrics)
            .order_by('-total_sales','product__name')
        )

        response.context_data['summary_total'] = dict(
            qs.filter(order__status='3').aggregate(**metrics)
        )

        return response

@admin.register(OrderReport)
class OrderReportAdmin(admin.ModelAdmin):
    change_list_template = 'storeApp/adminOrderReport.html'
    date_hierarchy = 'date' # 通过日期过滤对象

    def changelist_view(self, request, extra_context={}):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total_price': Sum('total_price'),
        }

        response.context_data['summary'] = list(
            qs
            .filter(status='3')
            .values('id')
            .annotate(**metrics)
            .order_by('-total_price',)
        )

        response.context_data['summary_total'] = dict(
            qs.filter(status='3').aggregate(**metrics)
        )

        return response

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'freight']
