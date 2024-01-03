from rest_framework import serializers

from django.shortcuts import get_object_or_404

from products.models import Category
from products.models import Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "slug",
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "slug",
            "price",
        )

    def create(self, validated_data: dict) -> Product:
        """
        Customizing to populate the validated data with
        owner and category information.
        """
        user = self.context["request"].user
        category_slug = self.context["view"].kwargs["category_slug"]

        validated_data["owner"] = user
        validated_data["category"] = get_object_or_404(Category, slug=category_slug)

        return Product.objects.create(**validated_data)
