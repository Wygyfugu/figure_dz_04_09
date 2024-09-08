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
    def __init__(self, side_a, side_b, side_c, half_meter, height):
        if side_a <= 0 or side_b <= 0 or side_c <= 0 or half_meter <= 0 or height <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.half_meter = half_meter
        self.height = height

    @property
    def perimeter(self, half_meter):
        return (self.side_a + self.side_b + self.side_c) / 2

    @property
    def height(self, height):
        return (
            2
            * (
                math.cbrt(
                    self.half_meter
                    * (self.half_meter - self.side_a)
                    * (self.half_meter - self.side_b)
                    * (self.half_meter - self.side_c)
                )
            )
            / self.side_a
        )

    @property
    def get_area(self):
        return 0.5 * self.side_a * self.height

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @height.setter
    def height(self, value):
        self._height = value


class Square(Triangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than 0")
        super().__init__(side_a, side_a)


t = Triangle(13, 14, 15)
s = Square(10)
print(s.add_area(t))
print(t.add_area(s))
