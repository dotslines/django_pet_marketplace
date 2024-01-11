from django import template
from django.contrib.admin.templatetags.admin_modify import submit_row
from django.contrib.admin.templatetags.base import InclusionAdminNode

register = template.Library()


def submit_row_no_delete(context):
    """
    Display the row of buttons for save without delete.
    """
    ctx = submit_row(context)
    ctx.update(
        {
            "show_delete_link": False,
        }
    )
    return ctx


@register.tag(name="submit_row_no_deletion")
def submit_row_no_deletion(parser, token):
    return InclusionAdminNode(parser, token, func=submit_row_no_delete, template_name="submit_line.html")
