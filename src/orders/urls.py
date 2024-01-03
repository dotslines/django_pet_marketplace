from django.urls import path

from .api import views

urlpatterns = [
    path("", views.OrdersListCreateAPIView.as_view()),
    path("<uuid:order_id>/", views.OrderDetailAPIView.as_view()),
]
