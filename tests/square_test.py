import pytest
from src.square import Square


def test_square_initialization_valid():
    square = Square(5)
    assert square.side_a == 5


def test_square_initialization_invalid():
    with pytest.raises(ValueError, match="Square sides can't be less than or equal to 0"):
        Square(0)
    with pytest.raises(ValueError, match="Square sides can't be less than or equal to 0"):
        Square(-1)


def test_square_get_area():
    square = Square(5)
    expected_area = 5**2
    assert square.get_area() == expected_area


def test_square_get_perimeter():
    square = Square(5)
    expected_perimeter = 4 * 5
    assert square.get_perimeter() == expected_perimeter
