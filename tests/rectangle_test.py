import pytest
from src.rectangle import Rectangle


def test_rectangle_initialization_valid():
    rectangle = Rectangle(3, 5)
    assert rectangle.side_a == 3
    assert rectangle.side_b == 5


def test_rectangle_initialization_invalid():
    with pytest.raises(ValueError, match="Rectangle sides can't be less than or equal to 0"):
        Rectangle(0, 5)
    with pytest.raises(ValueError, match="Rectangle sides can't be less than or equal to 0"):
        Rectangle(3, 0)
    with pytest.raises(ValueError, match="Rectangle sides can't be less than or equal to 0"):
        Rectangle(-1, 5)
    with pytest.raises(ValueError, match="Rectangle sides can't be less than or equal to 0"):
        Rectangle(3, -1)


def test_rectangle_get_area():
    rectangle = Rectangle(3, 5)
    expected_area = 3 * 5
    assert rectangle.get_area() == expected_area


def test_rectangle_get_perimeter():
    rectangle = Rectangle(3, 5)
    expected_perimeter = (3 + 5) * 2
    assert rectangle.get_perimeter() == expected_perimeter
