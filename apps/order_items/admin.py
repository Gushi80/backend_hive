from django.contrib import admin
from apps.order_items.models import OrderItem

# Register your models here.
@admin.register(OrderItem)
class OrderItemModel(admin.ModelAdmin):
    fields=['order','product','qty']
    list_filter = []
    list_display = fields
    search_fields = ['order']
