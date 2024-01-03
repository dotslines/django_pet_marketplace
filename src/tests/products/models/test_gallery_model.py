from products.models import Gallery


def test_gallery_model_str(product_gallery: Gallery) -> None:
    assert product_gallery.__str__() == "gallery name"
