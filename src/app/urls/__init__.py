import debug_toolbar
from rest_framework_jwt.views import obtain_jwt_token

from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path

api = [
    path("v1/", include("app.urls.v1")),
]

urlpatterns = [
    path("api/", include(api)),
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    re_path(r"^api-token-auth/", obtain_jwt_token),
]
