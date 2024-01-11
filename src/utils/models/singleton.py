from typing import Any

from django.db import models


class Singleton(models.Model):
    class Meta:
        abstract = True

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args: Any, **kwargs: Any) -> None:
        "Assumed that should not be deletion."

    @classmethod
    def load(cls) -> models.Model:
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
