import pytest
import math
from src.triangle import Triangle


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        (13, 14, 15),
    ],
)
def test_triangle_initialization_valid(side_a, side_b, side_c):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.side_a == side_a
    assert triangle.side_b == side_b
    assert triangle.side_c == side_c


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        (0, 14, 15),
        (13, 0, 15),
        (13, 14, 0),
        (-1, 14, 15),
        (13, -1, 15),
        (13, 14, -1),
    ],
)
def test_triangle_initialization_invalid(side_a, side_b, side_c):
    with pytest.raises(
        ValueError, match="Triangle sides can't be less than or equal to 0"
    ):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        (13, 14, 15),
    ],
)
def test_triangle_get_area(side_a, side_b, side_c):
    triangle = Triangle(side_a, side_b, side_c)
    s = (side_a + side_b + side_c) / 2
    expected_area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    assert triangle.get_area() == pytest.approx(expected_area, rel=1e-9)


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [
        (13, 14, 15),
    ],
)
def test_triangle_get_perimeter(side_a, side_b, side_c):
    triangle = Triangle(side_a, side_b, side_c)
    expected_perimeter = side_a + side_b + side_c
    assert triangle.get_perimeter() == expected_perimeter
