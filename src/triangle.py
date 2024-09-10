from figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides can't be less than or equal to 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.half_meter = (side_a + side_b + side_c) / 2

    def get_area(self):
        # Calculate the height for the area
        root = math.sqrt(
            self.half_meter
            * (self.half_meter - self.side_a)
            * (self.half_meter - self.side_b)
            * (self.half_meter - self.side_c)
        )
        return root

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


t = Triangle(13, 14, 15)
print(t.add_area)
print(t.get_area(), t.get_perimeter())
