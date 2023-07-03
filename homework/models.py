from typing import Dict
from copy import copy


class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity: int) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        stock_quantity = copy(self.quantity)
        check = stock_quantity - quantity
        is_available = True if check >= 0 else False
        return is_available

    def buy(self, quantity: int) -> bool:
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        quantity_check = self.check_quantity(quantity=quantity)
        if not quantity_check:
            raise ValueError(
                f'Невозможно купить товар. Запрашиваемое кол-во: {quantity}, складские запасы {self.quantity}.'
            )
        else:
            self.quantity -= quantity
            return True

    def __hash__(self) -> int:
        return hash(self.name + self.description)

    def __repr__(self) -> str:
        return self.name


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    """
    # Словарь продуктов и их количество в корзине
    products: Dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1) -> None:
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество.
        """
        if product in self.products.keys():
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count: int = None) -> None:
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция.
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция.
        """
        if product in self.products.keys():
            if remove_count is None:
                del self.products[product]
            elif remove_count >= self.products[product]:
                del self.products[product]
            elif remove_count < self.products[product]:
                self.products[product] -= remove_count
        else:
            raise ValueError(f'Товар {product.name} отсутствует в корзине.')

    def clear(self) -> None:
        """
        Очистка корзины.
        """
        self.products = {}

    def get_total_price(self) -> float:
        total = float(0)
        for product in self.products:
            total += product.price * self.products[product]
        return total

    def buy(self) -> None:
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError.
        """
        for product in self.products:
            try:
                product.buy(quantity=self.products[product])
            except ValueError as e:
                raise e
            else:
                self.clear()


if __name__ == '__main__':
    prod_1 = Product(
        name='prod_1',
        price=100,
        description='prod_1 desc',
        quantity=10
    )
    prod_2 = Product(
        name='prod_2',
        price=100,
        description='prod_2 desc',
        quantity=10
    )
    cart = Cart()
    # cart.products[prod_1] = 1
    # cart.products[prod_2] = 2
    cart.add_product(product=prod_1)
    cart.add_product(product=prod_1)
    cart.add_product(product=prod_2, buy_count=3)
    total_price = cart.get_total_price()
    cart.buy()
    print(cart)
    # cart.remove_product(product=prod_2)
    # print(cart)
    # cart.remove_product(product=prod_2, remove_count=1)
    # print(cart)