from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveAPIView

from utils.permissions import ObjectOwnerPermission

from ..models import Order
from .serializers import OrderSerializer


class OrdersListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects
    permission_classes = (ObjectOwnerPermission,)
    serializer_class = OrderSerializer


class OrderDetailAPIView(RetrieveAPIView):
    permission_classes = (ObjectOwnerPermission,)
    serializer_class = OrderSerializer
