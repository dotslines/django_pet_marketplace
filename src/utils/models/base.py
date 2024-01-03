from django.db import models

from .timestamp import DateTimeStampMixin
from .visibility import VisibilityMixin


class BaseQueryset(models.QuerySet):
    """Queryset with some general methods."""

    def visible(self) -> models.QuerySet:
        """Return only instances with visible status."""
        return self.filter(visible=True)


BaseManager = models.Manager.from_queryset(BaseQueryset)


class BaseModel(DateTimeStampMixin, VisibilityMixin):
    """Base abstract model."""

    objects = BaseManager()

    class Meta:
        abstract = True
