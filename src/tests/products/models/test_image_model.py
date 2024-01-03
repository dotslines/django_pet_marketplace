from products.models import Image


def test_image_model_str(product_image: Image) -> None:
    assert product_image.__str__() == "image name"
