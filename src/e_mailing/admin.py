from django.contrib import admin

from e_mailing.models import Email


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = "from_email", "to_email"
    list_filter = "created", "updated"
    date_hierarchy = "created"
    search_fields = "from_email", "to_email"
    readonly_fields = "created", "updated"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "from_email",
                    "to_email",
                    "reply_to",
                    "subject",
                    "body",
                    "sent_timestamp",
                    "status",
                )
            },
        ),
        (
            "DateTime Stamps",
            {
                "fields": (
                    "created",
                    "updated",
                )
            },
        ),
    )
