"""
Протестируйте классы из модуля homework/models.py
"""
from dataclasses import dataclass

import pytest

from homework.models import Product, Cart


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

    @pytest.fixture(scope='function', params=[product_1, 1, product_2, 1])
    def cart_with_products(
            self,
            product_1: Product = product_1,
            product_1_quantity: int = 1,
            product_2: Product = product_2,
            product_2_quantity: int = 1,
    ) -> CartWithProducts:
        cart = Cart()
        cart.add_product(product=product_1, buy_count=product_1_quantity)
        cart.add_product(product=product_2, buy_count=product_2_quantity)
        fixture = CartWithProducts(
            cart=cart,
            product_1=product_1,
            product_2=product_2
        )
        return fixture

    def test_add_products_to_cart(self, cart_with_products):
        assert cart_with_products.cart.products[cart_with_products.product_1] == 10
        assert cart_with_products.cart.products[cart_with_products.product_1] == 20

    # @pytest.mark.parametrize(
    #     'expected_sum', [200, 10000, 20000]
    # )
    # def test_products_cart_sum(self, cart_with_products, expected_sum):
    #     total_sum = cart_with_products.cart.get_total_price()
    #     assert total_sum == expected_sum

    @pytest.mark.parametrize(
        'cart_with_products', [
            pytest.lazy_fixture('product_1'), 10, pytest.lazy_fixture('product_2'), 20
        ], indirect=True
    )
    def test_products_cart_sum(self, cart_with_products):
        total_sum = cart_with_products.cart.get_total_price()
        assert total_sum == 20000