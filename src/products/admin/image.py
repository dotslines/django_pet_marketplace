from django.contrib import admin

from products.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = "name", "slug", "visible"
    list_editable = ("visible",)
    list_filter = "created", "updated"
    search_fields = "name", "slug"
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = "created", "updated"
    list_select_related = ("gallery",)
    fieldsets = (
        (
            None,
            {"fields": ("visible", "gallery", "name", "slug", "title", "alt")},
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
