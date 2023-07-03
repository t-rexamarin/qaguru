"""
Протестируйте классы из модуля homework/models.py
"""
from dataclasses import dataclass

import pytest

from models import Product, Cart


@pytest.fixture(scope='function')
def product_1() -> Product:
    """
    Тестовый продукт
    """
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture(scope='function')
def product_2() -> Product:
    """
    Тестовый продукт
    """
    return Product("hook", 100, "This is a hook", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    @pytest.mark.parametrize(
        'buy_quantity, expected_result',
        [
            (1, True),
            (1000, True),
            (1001, False)
        ]
    )
    def test_product_check_quantity(self, product_1, buy_quantity, expected_result):
        # TODO напишите проверки на метод check_quantity
        result = product_1.check_quantity(quantity=buy_quantity)
        assert result is expected_result

    @pytest.mark.parametrize(
        'buy_quantity, expected_result',
        [
            (1, True),
            (1000, True)
        ]
    )
    def test_product_buy(self, product_1, buy_quantity, expected_result):
        # TODO напишите проверки на метод buy
        result = product_1.buy(quantity=buy_quantity)
        assert result is expected_result

    def test_product_buy_more_than_available(self, product_1):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product_1.buy(quantity=product_1.quantity + 1)


@dataclass
class CartWithProducts:
    cart: Cart
    product_1: Product
    product_2: Product


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    @pytest.fixture(scope='function')
    def empty_cart(self) -> Cart:
        cart = Cart()
        return cart

    @pytest.mark.parametrize(
        'product_quantity, expected_result', [(1, 1), (5, 5)]
    )
    def test_add_products_to_cart(self, empty_cart, product_1, product_quantity, expected_result):
        empty_cart.add_product(product=product_1, buy_count=product_quantity)
        assert empty_cart.products[product_1] == expected_result

    @pytest.mark.parametrize(
        'product_1_quantity, product_2_quantity, total_sum',
        [
            (1, 2, 300), (2, 4, 600)
        ]
    )
    def test_products_cart_sum(
            self,
            empty_cart,
            product_1,
            product_2,
            product_1_quantity,
            product_2_quantity,
            total_sum
    ):
        empty_cart.add_product(product=product_1, buy_count=product_1_quantity)
        empty_cart.add_product(product=product_2, buy_count=product_2_quantity)
        _sum = empty_cart.get_total_price()
        assert _sum == total_sum
