from src.Rectangle import Rectangle
import pytest

@pytest.mark.smoke
def test_rectangle_integer():
r = Rectangle(side_a:3, side_b:5)
assert r.get_area == 15, 'Area should be 15'

@pytest.mark.slow
def test_rectangle_float():
r = Rectangle(side_a:3.5, side_b:5.5)
assert r.get_area == 19.25, 'Area should be 19.25'
