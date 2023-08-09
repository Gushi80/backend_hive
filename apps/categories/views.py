from django.shortcuts import render
from rest_framework import generics
from .models import Categories
from .serializers import CategorySerializer


# Create your views here.

class CategoryList(generics.ListAPIView):
    serializer_class=CategorySerializer
    query_set= Categories.objects.all()
    pagination_class=None