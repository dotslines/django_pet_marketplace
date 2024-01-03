import pytest

from pytest_factoryboy import register

from tests.products import factories

register(factories.BrandFactory)  # returns brand_factory fixture
register(factories.CategoryFactory)  # returns category_factory fixture
register(factories.ProductFactory)  # returns product_factory fixture
register(factories.GalleryFactory)  # returns gallery_factory fixture
register(factories.ImageFactory)  # returns image_factory fixture


@pytest.fixture()
def product_brand(db, brand_factory):
    brand = brand_factory.create()
    return brand


@pytest.fixture()
def product_category(db, category_factory):
    category = category_factory.create()
    return category


@pytest.fixture()
def product(db, product_factory):
    product = product_factory.create()
    return product


@pytest.fixture()
def product_gallery(db, gallery_factory):
    gallery = gallery_factory.create()
    return gallery


@pytest.fixture()
def product_image(db, image_factory):
    image = image_factory.create()
    return image
