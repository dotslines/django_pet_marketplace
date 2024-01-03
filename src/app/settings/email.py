from app.settings.environ import env

EMAIL_HOST = env("EMAIL_HOST", default="")
EMAIL_PORT = env("EMAIL_PORT", default="")
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = ""
DEFAULT_REPLY_TO = DEFAULT_FROM_EMAIL  # noqa: F821
