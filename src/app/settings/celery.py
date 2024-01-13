from celery.schedules import crontab

from app.settings.environ import env

CELERY_TIMEZONE = "Australia/Tasmania"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

if env("DEBUG", cast=bool):
    CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
    CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
else:
    CELERY_BROKER_URL = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND = "redis://redis:6379/0"

CELERYBEAT_SCHEDULE = {
    "send-created-per-day-orders-report": {
        "task": "orders.tasks.send_amount_of_new_orders_to_manager",
        "schedule": crontab(minute=30, hour=0),
    },
}
