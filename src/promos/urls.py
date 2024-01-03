from django.urls import path

from promos.api import views

urlpatterns = [
    path("", views.PromosListCreateAPIView.as_view()),
    path("<slug:promo_slug>/", views.PromoDetailAPIView.as_view()),
]
