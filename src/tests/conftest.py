import pytest
from typing import Generator

from django.core.cache import cache
from django.http import HttpRequest

pytest_plugins = [
    "tests.accounts.factories",
    "tests.accounts.fixtures",
    "tests.products.factories",
    "tests.products.fixtures",
]


@pytest.fixture(autouse=True)
def _clear_django_cache(request: HttpRequest) -> Generator:
    """
    Clear django cache at the end of each test.
    """
    yield
    cache.clear()
