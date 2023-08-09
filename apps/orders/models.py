from django.db import models
from apps.users.models import User
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    class Meta(object):
        db_table='order'
    user=models.ForeignKey(
        User, related_name='related_order_user',on_delete=models.CASCADE
    ) 
    customer_name=models.CharField(
        'customer name', blank=False, null=False, max_length=150
    )
    customer_phone=models.CharField(
        'customer phone', blank=False, null=False, max_length=200
    )
    customer_address=models.CharField(
        'customer address', blank=False, null=False, max_length=200
    ) 
    pin_code=models.CharField(
        'pin code', blank=False, null=False, max_length=100
    )
    building_number=models.CharField(
        'building', blank=False, null=False, max_length=120
    )
    city=models.CharField(
        'city', blank=False, null=False, max_length=100
    ) 
    state=models.CharField(
        'state',blank=False, null=False, max_length=130
    ) 
    total_price=models.FloatField(
        'total price', blank=False, null=False
    )
    total_quantity=models.IntegerField(
        'total quantity', blank=False, null=False
    )
    created_at=models.DateTimeField(
        'creation date', blank=True, default=timezone.now
    )

    @property
    def order_items(self):
        return self.related_order.all()