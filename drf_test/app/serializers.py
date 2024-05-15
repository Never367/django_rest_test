from typing import Any

from rest_framework import serializers
from .models import Products, Reviews


class ProductsSerializer(serializers.ModelSerializer):
    # Serialization of product data
    class Meta:
        model = Products
        fields = ['asin', 'title']


class ReviewsSerializer(serializers.ModelSerializer):
    # Serialization of reviews data
    class Meta:
        model = Reviews
        fields = ['asin', 'title', 'review']

    def create(self, validated_data: dict[str, Any]) -> Reviews:
        return Reviews.objects.create(**validated_data)
