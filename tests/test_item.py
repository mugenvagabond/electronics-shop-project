import pytest
from src.item import Item
from src.phone import Phone


def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    with pytest.raises(Exception, match='Длина наименования товара превышает 10 символов'):
        item.name = 'Телекоммуникатор'


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item1):
    assert str(item1) == "Смартфон"


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_apply_discount(item1):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_add(item1):
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
