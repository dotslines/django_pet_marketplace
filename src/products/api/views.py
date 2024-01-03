from typing import Any

from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from products.api.serializers import CategorySerializer
from products.api.serializers import ProductSerializer
from products.models import Category
from products.models import Product
from utils.permissions import ObjectOwnerPermission
from utils.view_mixins import MultipleLookupFieldsMixin


class CategoriesListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects


class CategoryAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request, category_slug: str) -> Response:
        category = get_object_or_404(Category, slug=category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=200)


class ProductsListCreateAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self) -> QuerySet[Product]:
        category = get_object_or_404(Category, slug=self.kwargs["category_slug"])
        products = category.products.all()
        return products


class ProductAPIView(MultipleLookupFieldsMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ObjectOwnerPermission]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_kwargs = {"slug": "product_slug", "category__slug": "category_slug"}

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        self.permission_classes = [AllowAny]
        return super().get(request, *args, **kwargs)
