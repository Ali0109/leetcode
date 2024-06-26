from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result


class ConcreteCreator1(Creator):
    def factory_method(self) -> 'Product':
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self) -> 'Product':
        return ConcreteProduct2()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    print(f"Client: {creator.some_operation()}", end="")

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
