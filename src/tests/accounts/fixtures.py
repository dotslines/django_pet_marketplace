import pytest

from pytest_factoryboy import register

from tests.accounts import factories

register(factories.BuyerFactory)  # returns buyer_factory fixture
register(factories.SellerFactory)  # returns seller_factory fixture


@pytest.fixture()
def buyer(db, buyer_factory):
    buyer = buyer_factory.create()
    return buyer


@pytest.fixture()
def seller(db, seller_factory):
    seller = seller_factory.create()
    return seller
