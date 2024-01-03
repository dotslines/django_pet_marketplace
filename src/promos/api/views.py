from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from promos.api.serializers import PromoSerializer
from promos.models import Promo
from utils.permissions import ObjectOwnerPermission


class PromosListCreateAPIView(ListCreateAPIView):
    queryset = Promo.objects
    serializer_class = PromoSerializer
    permission_classes = [IsAuthenticated]


class PromoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Promo.objects
    serializer_class = PromoSerializer
    permission_classes = [IsAuthenticated, ObjectOwnerPermission]
