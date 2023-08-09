from rest_framework.fields import ImageField
from .models import Categories
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    image= ImageField(read_only=True)

    class Meta:
        model=Categories
        fields= '__all__'

    def validate(self, data):
        errors={}
        if 'name' not in data:
            errors['name']=['name is required']

        if bool(errors):
            raise serializers.ValidationError(errors)
        
        return data