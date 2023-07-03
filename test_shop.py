import pytest

from models import Product, Cart


@pytest.fixture(scope='function')
def product_1() -> Product:
    """
    Тестовый продукт 1.
    """
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture(scope='function')
def product_2() -> Product:
    """
    Тестовый продукт 2.
    """
    return Product("hook", 100, "This is a hook", 1000)


class TestProducts:
    """
    Тесты про Product.
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
        """
        Проверка на метод Product.check_quantity.
        """
        result = product_1.check_quantity(quantity=buy_quantity)
        assert result is expected_result,\
            f'Product.check_quantity не прошел проверку. Ожидали {expected_result}, вернулось {result}.'

    @pytest.mark.parametrize(
        'buy_quantity, expected_result',
        [
            (1, True),
            (1000, True)
        ]
    )
    def test_product_buy(self, product_1, buy_quantity, expected_result):
        """
        Проверка на метод Product.buy.
        """
        result = product_1.buy(quantity=buy_quantity)
        assert result is expected_result,\
            f'Product.buy не прошел проверку. Ожидали {expected_result}, вернулось {result}.'

    def test_product_buy_more_than_available(self, product_1):
        """
        Негативная проверка на метод Product.buy.
        """
        with pytest.raises(ValueError):
            product_1.buy(quantity=product_1.quantity + 1)


class TestCart:
    """
    Кейсы на корзину.
    """
    @pytest.fixture(scope='function')
    def empty_cart(self) -> Cart:
        """
        Объект пустой корзины.
        """
        cart = Cart()
        return cart

    @pytest.mark.parametrize(
        'product_quantity, expected_result', [(1, 1), (5, 5)]
    )
    def test_add_products_to_cart(self, empty_cart, product_1, product_quantity, expected_result):
        """
        Проверка Cart.add_product.
        """
        empty_cart.add_product(product=product_1, buy_count=product_quantity)
        assert empty_cart.products[product_1] == expected_result,\
            f'Cart.add_product не прошел проверку. Ожидали {expected_result}, ' \
            f'вернулось {empty_cart.products[product_1]}.'

    @pytest.mark.parametrize(
        'product_1_quantity, product_2_quantity, expected_total_sum',
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
            expected_total_sum
    ):
        """
        Проверка Cart.get_total_price.
        """
        empty_cart.add_product(product=product_1, buy_count=product_1_quantity)
        empty_cart.add_product(product=product_2, buy_count=product_2_quantity)
        _sum = empty_cart.get_total_price()
        assert _sum == expected_total_sum,\
            f'Cart.get_total_price не прошел проверку. Ожидали {expected_total_sum}, вернулось {_sum}.'

    @pytest.mark.parametrize(
        'product_1_add_quantity, product_2_add_quantity, product_1_delete_quantity, product_2_delete_quantity, '
        'product_1_expected_quantity, product_2_expected_quantity',
        [
            (2, 2, 1, 1, 1, 1), (4, 4, 2, 3, 2, 1)
        ]
    )
    def test_cart_remove_product(
            self,
            empty_cart,
            product_1,
            product_2,
            product_1_add_quantity,
            product_2_add_quantity,
            product_1_delete_quantity,
            product_2_delete_quantity,
            product_1_expected_quantity,
            product_2_expected_quantity
    ):
        """
        Проверка Cart.remove_product.
        Добавление товара в корзину. Удаление части товаров. Проверка итогового кол-ва.
        :param empty_cart:
        :param product_1:
        :param product_2:
        :param product_1_add_quantity: сколько добавить product_1
        :param product_2_add_quantity: сколько добавить product_2
        :param product_1_delete_quantity: сколько удалить product_1
        :param product_2_delete_quantity: сколько удалить product_2
        :param product_1_expected_quantity: сколько ожидаем в конце product_1
        :param product_2_expected_quantity: сколько ожидаем в конце product_2
        """
        empty_cart.add_product(product=product_1, buy_count=product_1_add_quantity)
        empty_cart.add_product(product=product_2, buy_count=product_2_add_quantity)
        empty_cart.remove_product(product=product_1, remove_count=product_1_delete_quantity)
        empty_cart.remove_product(product=product_2, remove_count=product_2_delete_quantity)
        assert empty_cart.products[product_1] == product_1_expected_quantity
        assert empty_cart.products[product_2] == product_2_expected_quantity

    @pytest.mark.parametrize(
        'remove_count', [1, None]
    )
    def test_cart_absolute_remove_product(self, empty_cart, product_1, remove_count):
        """
        Проверка Cart.remove_product.
        Полное удаление продукта из корзины.
        """
        empty_cart.add_product(product=product_1, buy_count=1)
        empty_cart.remove_product(product=product_1, remove_count=remove_count)
        product = empty_cart.products.get(product_1)
        assert product is None
