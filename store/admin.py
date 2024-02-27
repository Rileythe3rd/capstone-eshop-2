from django.contrib import admin
from .models import Product
from django.core.management import call_command

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        call_command('collect_static_images')

admin.site.register(Product, ProductAdmin)