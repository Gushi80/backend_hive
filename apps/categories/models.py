from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Categories(models.Model):
    class Meta(object):
        db_table="category"
        verbose_name_plural="Categories"
    name=models.CharField(
        'name', blank=False, null=False, max_length=100
    )
    image=CloudinaryField(
        "Category image", blank=True, null=True
    )
    created_at=models.DateTimeField(
        'creation date', blank=True, null=True, auto_now_add=True
    )
    updated_at=models.DateTimeField(
        'updation date', blank=True, null=True, auto_now_add=True
    )

    def __str__(self):
        return self.name