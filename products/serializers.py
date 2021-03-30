from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    price = serializers.DecimalField(
        decimal_places=2, max_digits=5)
