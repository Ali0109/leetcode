class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


vector1 = Vector2D(1, 2)
vector2 = Vector2D(3, 4)
print("Vector sum:", vector1 + vector2)
print("Vector sum:", vector1 - vector2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Point(self.x + vector.x, self.y + vector.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


point = Point(5, 6)

print("Point sum:", point + vector2)
