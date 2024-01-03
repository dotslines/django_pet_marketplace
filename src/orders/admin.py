import json

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = "id", "visible", "owner"
    list_editable = ("visible",)
    list_filter = "created", "updated"
    search_fields = "id", "owner"
    readonly_fields = "id", "created", "updated", "products_pretty_view", "promos"
    change_form_template = "admin/change_form.html"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "visible",
                    "owner",
                )
            },
        ),
        (
            "Products",
            {
                "fields": (
                    "products_pretty_view",
                    "products",
                )
            },
        ),
        (
            "Promotions",
            {"fields": ("promos",)},
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

    @admin.display(description=_("Ordered Products(readonly field)"))
    def products_pretty_view(self, instance: Order) -> str:
        "prepares formated/pretty print for JSON field"
        products = json.dumps(instance.products, indent=2)
        formatter = HtmlFormatter(style="colorful")
        products = highlight(products, JsonLexer(), formatter)
        style = "<style>" + formatter.get_style_defs() + "</style><br>"
        return mark_safe(style + products)

    @admin.display(description=_("Promotions used(readonly field)"))
    def promos(self, instance: Order) -> str:
        "prepares formated/pretty print for JSON field"
        promos = json.dumps(instance.promos, indent=2)
        formatter = HtmlFormatter(style="colorful")
        promos = highlight(promos, JsonLexer(), formatter)
        style = "<style>" + formatter.get_style_defs() + "</style><br>"
        return mark_safe(style + promos)
