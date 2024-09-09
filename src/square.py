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
        return self.get_area() + other_figure.get_area()

class Square(Figure):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than or equal to 0")
        self.side_a = side_a

    def get_area(self):
        return self.side_a ** 2

    def get_perimeter(self):
        return 4 * self.side_a


s = Square(5)
print(s.get_area())
print(s.get_perimeter())
