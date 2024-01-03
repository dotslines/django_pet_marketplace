from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveAPIView

from utils.permissions import ObjectOwnerPermission

from .serializers import OrderSerializer


class OrdersListCreateAPIView(ListCreateAPIView):
    permission_classes = (ObjectOwnerPermission,)
    serializer_class = OrderSerializer


class OrderDetailAPIView(RetrieveAPIView):
    permission_classes = (ObjectOwnerPermission,)
    serializer_class = OrderSerializer
