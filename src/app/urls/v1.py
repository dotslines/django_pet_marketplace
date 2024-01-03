from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView

from django.urls import include
from django.urls import path

urlpatterns = [
    path("healthchecks/", include("django_healthchecks.urls")),
    # Docs
    path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("docs/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # Apps
    path("orders/", include("orders.urls")),
    path("promos/", include("promos.urls")),
    path("", include("products.urls")),
]
