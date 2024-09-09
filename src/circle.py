from abc import ABC, abstractmethod
import math
from math import pi

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a Figure")
        return self.get_area() + other_figure.get_area()


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Triangle sides can't be less than or equal to 0")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


class Square(Circle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than or equal to 0")
        super().__init__(side_a)


# Example usage
c = Circle(5)
s = Square(10)
print(s.add_area(c))
print(c.add_area(s))

