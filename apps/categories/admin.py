from django.contrib import admin 
from .models import Categories

# Register your models here.
@admin.register(Categories)
class CategoryModel(admin.ModelAdmin):
    fields=['name','image']
    list_filter=[]
    list_display=fields
    search_fields=['name']