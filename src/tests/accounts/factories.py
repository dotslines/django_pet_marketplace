import factory
from faker import Faker

fake = Faker()


class BuyerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.Buyer"

    username = "eat_my_shorts"
    email = "eat_my_shorts@karamba.sprngfld"
    first_name = "Bart"
    last_name = "Simpson"


class SellerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.Seller"

    username = "moe"
    email = "moammar_szyslak@tavern.sprngfld"
    first_name = "Moe"
    last_name = "Szyslak"
