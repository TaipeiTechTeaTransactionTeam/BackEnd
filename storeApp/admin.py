from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from .models import Product
from .models import Store
from .models import TeaType
from .models import Order, OrderContainProduct
from .models import SeasoningDiscount
from .models import ShippingDiscount
from .models import ProductDiscount
from .models import Report


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

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    change_list_template = 'storeApp/adminReport.html'
    date_hierarchy = 'date' # 通过日期过滤对象
    # list_display = ['id', 'own_user']

    def get_total(self,request):
        #functions to calculate whatever you want...
        total = len(super().get_queryset(request))
        return total

    def get_totalPrice(self):
        #functions to calculate whatever you want...
        price = 0
        report = Report.objects.all()
        for r in report:
            price = r.total_price
        return price

    def changelist_view(self, request, extra_context={}):
        extra_context['total'] = self.get_total(request)
        extra_context['price'] = self.get_totalPrice()
        return super(ReportAdmin, self).changelist_view(request,
            extra_context)

    def response_change(self, request, obj):
        if "day" in request.POST:
            self.message_user(request, "day")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)

admin.site.register(Store)
