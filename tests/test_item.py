"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


item1 = Item('item_1', 100, 2)
def test_item():
    assert type(Item.all) is list
    assert type(Item.pay_rate) is float
    assert item1.calculate_total_price() == 20.0
    assert item1.apply_discount() is None


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5