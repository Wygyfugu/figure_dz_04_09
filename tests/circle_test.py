import pytest
import math
from src.circle import Circle


@pytest.mark.parametrize("radius", [5])
def test_circle_initialization_valid(radius):
    circle = Circle(radius)
    assert circle.radius == radius


@pytest.mark.parametrize("radius", [0, -1])
def test_circle_initialization_invalid(radius):
    with pytest.raises(ValueError, match="Radius must be greater than 0"):
        Circle(radius)


@pytest.mark.parametrize(
    "radius, expected_area",
    [
        (5, math.pi * 5**2),
        (10, math.pi * 10**2),
    ],
)
def test_circle_get_area(radius, expected_area):
    circle = Circle(radius)
    assert circle.get_area() == pytest.approx(expected_area, rel=1e-9)


@pytest.mark.parametrize(
    "radius, expected_perimeter",
    [
        (5, 2 * math.pi * 5),
        (10, 2 * math.pi * 10),
    ],
)
def test_circle_get_perimeter(radius, expected_perimeter):
    circle = Circle(radius)
    assert circle.get_perimeter() == pytest.approx(expected_perimeter, rel=1e-9)
