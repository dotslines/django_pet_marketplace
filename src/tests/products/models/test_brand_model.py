from products.models import Brand


def test_brand_model_str(product_brand: Brand) -> None:
    assert product_brand.__str__() == "brand name"
