import pytest
from src.item import Item


@pytest.fixture
def item3():
    return Item("ПК", 100000, 1)


def test_calculate_total_price(item3):
    assert item3.calculate_total_price() == 100000


def test_apply_discount(item3):
    Item.pay_rate = 0.8
    item3.apply_discount()
    assert item3.price == 80000.0
