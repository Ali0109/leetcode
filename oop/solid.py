from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class AreaCalculator:

    def calculate(self, shapes: list[Shape]):
        total_area = 0
        for shape in shapes:
            total_area += shape.area()
        return total_area


calculator = AreaCalculator()
total_area = calculator.calculate(
    [
        Circle(5),
        Square(3)
    ]
)
print(total_area)
