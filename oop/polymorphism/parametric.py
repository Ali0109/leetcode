from typing import TypeVar

T = TypeVar("T")


def swap(a: T, b: T) -> None:
    a, b = b, a
    print("Swapped values:", a, b)


if __name__ == "__main__":
    int1, int2 = 5, 10
    double1, double2 = 3.14, 6.28
    char1, char2 = "a", "b"

    print("Before swap:")
    print("int1 =", int1, ", int2 =", int2)
    print("double1 =", double1, ", double2 =", double2)
    print("char1 =", char1, ", char2 =", char2)

    swap(int1, int2)
    swap(double1, double2)
    swap(char1, char2)
