"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item, item1


def test_item():
    assert type(Item.all) is list
    assert type(Item.pay_rate) is float
    assert item1.calculate_total_price() == 20.0
    assert item1.apply_discount() is None
