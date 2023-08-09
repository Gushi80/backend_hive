from django.db import models
from cloudinary.models import CloudinaryField
from apps.categories.models import Categories
from gd_backend.constants import PRODUCT_TYPE


# Create your models here.
class Product (models.Model):
    class Meta(object):
        db_table="product"
    name=models.CharField(
        'Name', blank=False, null=False, max_length=200
    )
    description=models.CharField(
        'Description', blank=True, null=True, max_length=250
    )
    price=models.FloatField(
        'Price', blank=False, null=False
    )
    image=CloudinaryField(
            'Product image',blank=True, null=True
        )
    type=models.CharField(
        'Type', blank=True, null=True, max_length=160, choices=PRODUCT_TYPE
    )
    category=models.ForeignKey(
        Categories, related_name='related_category', on_delete=models.CASCADE
    )


    def __str__(self):
        return self.name

