from abc import ABC, abstractmethod
import math

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
        return self.get_area + other_figure.get_area
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c, side_h, side_p):
        if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_h <= 0 or side_p <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_h = side_h
        self.side_p = side_p

    @property
    def half_meter(self, side_p):
        return (self.side_a + self.side_b + self.side_c) / 2

    @property
    def height(self, side_h):
        return 2 * (math.cbrt(self.side_p * (self.side_p - self.side_a) * (self.side_p - self.side_b)
                              * (self.side_p - self.side_c))) / self.side_a

    @property
    def get_area(self):
        return 0.5 * self.side_a * self.side_h

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

class Square(Triangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than 0")
        super().__init__(side_a, side_a)

t = Triangle(13, 14, 15)
s = Square(10)
print(s.add_area(t))
print(t.add_area(s))