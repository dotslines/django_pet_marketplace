from typing import Dict

from rest_framework.generics import GenericAPIView

from django.db.models import Model
from django.shortcuts import get_object_or_404


class MultipleLookupFieldsMixin(GenericAPIView):
    """
    The view sould have 'lookup_kwargs' implemented, as following:
        lookup_kwargs = {
            'model_field': 'url_kwarg_field',
            .....
        }
    """

    lookup_kwargs: Dict = dict()

    def get_object(self) -> Model:
        """
        get_object method overrided in order to let
        get the object using the multiple url kwargs.
        """
        queryset = self.filter_queryset(self.get_queryset())

        filter_kwargs = {}
        for k, v in self.lookup_kwargs.items():
            filter_kwargs[k] = self.kwargs[v]
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)
        return obj
