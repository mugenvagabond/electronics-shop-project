import pytest
from src.phone import Phone
from src.item import Item


def test_name():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.name = 'iPhone 14'
    assert phone1.name == 'iPhone 14'
    assert phone1.number_of_sim == 2


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone1):
    assert str(phone1) == "iPhone 14"


def test_calculate_total_price(phone1):
    assert phone1.calculate_total_price() == 600_000


def test_add(phone1):
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

