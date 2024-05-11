class Product:
    def __init__(self, name: str, package_code: str = "шт"):
        self.name = name
        self.package_code = self.validate_package_code(package_code)

    package_code_list = ["шт", "кг"]

    def validate_package_code(self, package_code):

        if package_code in self.package_code_list:
            return package_code
        else:
            raise ValueError(
                "Package code is not valid.\n"
                f"Available package codes: {self.package_code_list}"
            )


class Item:
    def __init__(
            self, product: Product,
            price: int, discount: int = 0,
            size: str = None
    ):
        self.product = product
        self.price = price
        self.size = self.validate_size(size)
        self.discount = discount

    size_list = ["S", "M", "L"]

    def validate_size(self, size):
        if size and size not in self.size_list:
            raise ValueError(
                "Size is not valid."
                f"Available sizes: {self.size_list}"
            )
        return size

    def get_total_price(self):
        return self.price * (self.discount // 100)

    def __repr__(self):
        return f"name={self.product.name};price={self.price}"


class ShoppingCartItem:
    def __init__(
            self, name: str,
            size: str, price: int,
            quantity: int
    ):
        self.name = name
        self.size = size
        self.quantity = quantity
        self.total_price = price


class ShoppingCartInterface:
    items = []

    def get_items(self):
        pass

    def add_item(self, *args, **kwargs):
        pass

    def remove_item(self, *args, **kwargs):
        pass

    def remove_all_items(self):
        pass


class ShoppingCart:
    items: list[ShoppingCartItem] = []

    def get_items(self):
        return self.items

    def add_item(self, item: Item, quantity: int):

        shopping_cart_item = ShoppingCartItem(
            name=item.product.name,
        )
        self.items.append(shopping_cart_item)

    def remove_item(self, item: Item, quantity: int):

        shopping_cart_item = ShoppingCartItem(
            name=item.product.name,
        )
        self.items.remove(shopping_cart_item)

    def remove_all_items(self):
        self.items = []

    def _search_item(self, **kwargs):
        for item in self.items:
            pass


class Calculator:

    @staticmethod
    def calculate_shopping_cart(shopping_cart: ShoppingCart) -> float:
        items = shopping_cart.get_items()
        total_price = 0
        for item in items:
            if item.discount:
                price = item.price * (item.discount // 100)
            else:
                price = item.price

            total_price += price
        return total_price


class Order:
    def __init__(self, shopping_cart: ShoppingCart):
        self.shopping_cart = shopping_cart

    def get_items(self):
        return self.shopping_cart.get_items()


class Printer:
    def print_order(self, order: Order):
        pass


apple = Product("apple", "кг")
banana = Product("banana", "кг")
chocolate = Product("chocolate", "шт")
apple_item = Item(apple, 100, discount=5)
shopping_cart = ShoppingCart()

shopping_cart.add_item(banana, 2)
shopping_cart.add_item(chocolate, 5)

total_price = Calculator.calculate_shopping_cart(shopping_cart)
print(total_price)
