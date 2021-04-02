from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=50)
    # price = serializers.DecimalField(
    #    decimal_places = 2, max_digits = 5)
    class Meta:
        model = Product
        fields = ('name', 'price')
