import pytest
import math
from src.circle import Circle


def test_circle_initialization_valid():
    circle = Circle(5)
    assert circle.radius == 5


def test_circle_initialization_invalid():
    with pytest.raises(ValueError, match="Radius must be greater than 0"):
        Circle(0)
    with pytest.raises(ValueError, match="Radius must be greater than 0"):
        Circle(-1)


def test_circle_get_area():
    circle = Circle(5)
    expected_area = math.pi * 5**2
    assert circle.get_area() == pytest.approx(expected_area, rel=1e-9)


def test_circle_get_perimeter():
    circle = Circle(5)
    expected_perimeter = 2 * math.pi * 5
    assert circle.get_perimeter() == pytest.approx(expected_perimeter, rel=1e-9)
