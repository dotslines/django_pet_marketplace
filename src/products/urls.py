from django.urls import path

from products.api import views

urlpatterns = [
    path("categories/", views.CategoriesListAPIView.as_view()),
    path("categories/<str:category_slug>/", views.CategoryAPIView.as_view()),
    path("categories/<str:category_slug>/products/", views.ProductsListCreateAPIView.as_view()),
    path("categories/<str:category_slug>/products/<str:product_slug>", views.ProductAPIView.as_view()),
]
