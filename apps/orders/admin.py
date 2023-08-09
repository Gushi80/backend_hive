from django.contrib import admin
from apps.orders.models import Order
# Register your models here.
@admin.register(Order)
class OrderModel(admin.ModelAdmin):
    fields = ['user','customer_name','customer_phone','customer_address','pin_code', 'building_number', 'city','state','total_price','total_quantity']
    list_filter = []
    list_display = fields
    search_fields = ['user']