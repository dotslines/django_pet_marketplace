from django import template
from django.contrib.admin.templatetags.admin_modify import submit_row
from django.contrib.admin.templatetags.base import InclusionAdminNode
from django.template.base import Parser
from django.template.base import Token
from django.template.context import Context
from django.template.context import RequestContext

register = template.Library()


def submit_row_no_delete(context: RequestContext) -> Context:
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
def submit_row_no_deletion(parser: Parser, token: Token) -> InclusionAdminNode:
    return InclusionAdminNode(parser, token, func=submit_row_no_delete, template_name="submit_line.html")
