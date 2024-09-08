from abc import ABC, abstractmethod


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
    def __init__(self, side_a, side_b, side_c, side_h):
        if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_h <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_h = side_h


class Square(Triangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than 0")
        super().__init__(side_a, side_a)

t = Triangle(13, 14, 15)
s = Square(10)
print(s.add_area(t))
print(t.add_area(s))