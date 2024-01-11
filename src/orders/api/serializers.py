from rest_framework import serializers

from ..models import Order
from ..services.order_postcreation import OrderPostCreation


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "owner", "products")

    def create(self, validated_data):
        instance = super().create(validated_data)
        OrderPostCreation(instance)

        return instance
