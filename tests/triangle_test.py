import pytest
import math
from src.triangle import Triangle


def test_triangle_initialization_valid():
    triangle = Triangle(13, 14, 15)
    assert triangle.side_a == 13
    assert triangle.side_b == 14
    assert triangle.side_c == 15


def test_triangle_initialization_invalid():
    with pytest.raises(ValueError, match="Triangle sides can't be less than or equal to 0"):
        Triangle(0, 14, 15)
    with pytest.raises(ValueError, match="Triangle sides can't be less than or equal to 0"):
        Triangle(13, 0, 15)
    with pytest.raises(ValueError, match="Triangle sides can't be less than or equal to 0"):
        Triangle(13, 14, 0)
    with pytest.raises(ValueError, match="Triangle sides can't be less than or equal to 0"):
        Triangle(-1, 14, 15)
    with pytest.raises(ValueError, match="Triangle sides can't be less than or equal to 0"):
        Triangle(13, -1, 15)
    with pytest.raises(ValueError, match="Triangle sides can't be less than or equal to 0"):
        Triangle(13, 14, -1)


def test_triangle_get_area():
    triangle = Triangle(13, 14, 15)
    s = (13 + 14 + 15) / 2
    expected_area = math.sqrt(s * (s - 13) * (s - 14) * (s - 15))
    assert triangle.get_area() == pytest.approx(expected_area, rel=1e-9)


def test_triangle_get_perimeter():
    triangle = Triangle(13, 14, 15)
    expected_perimeter = 13 + 14 + 15
    assert triangle.get_perimeter() == expected_perimeter
