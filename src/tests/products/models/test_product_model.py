from products.models import Product


def test_product_model_str(product: Product) -> None:
    assert product.__str__() == "product name"
    assert product.owner.username == "moe"
    assert product.owner.status == "seller"
