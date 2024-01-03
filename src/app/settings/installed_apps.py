# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_spectacular",
    "drf_spectacular_sidecar",  # required for Django collectstatic discovery
    "debug_toolbar",
    "rest_framework_jwt",
    "rest_framework_jwt.blacklist",
    "accounts",
    "e_mailing",
    "orders",
    "products",
    "promos",
    "utils",
]
