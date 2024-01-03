from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from django.views import View

from utils.custom_types import ModelWithOwnerFK


class ObjectOwnerPermission(BasePermission):
    """
    Checks if user tries to access an own object.
    """

    def has_object_permission(self, request: Request, view: View, obj: ModelWithOwnerFK) -> bool:
        return obj.owner.id == request.user.id
