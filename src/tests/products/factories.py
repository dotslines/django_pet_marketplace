import factory
from faker import Faker

from tests.accounts.factories import SellerFactory

fake = Faker()


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Brand"

    name = "brand name"
    slug = "brand slug"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Category"

    name = "category name"
    slug = "category slug"


class GalleryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Gallery"

    name = "gallery name"
    slug = "gallery slug"


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Image"

    gallery = factory.SubFactory(GalleryFactory)
    name = "image name"
    slug = "image slug"
    image = "path/to/image"
    title = "image title"
    alt = "image alt"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "products.Product"

    owner = factory.SubFactory(SellerFactory)
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)
    gallery = factory.SubFactory(GalleryFactory)
    name = "product name"
    slug = "product slug"
    price = 100.00
    sku = "product sku"
