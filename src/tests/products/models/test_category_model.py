from products.models import Category


def test_category_model_str(product_category: Category) -> None:
    assert product_category.__str__() == "category name"
