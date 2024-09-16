import pytest
from src.square import Square


@pytest.mark.parametrize("side_a", [5])
def test_square_initialization_valid(side_a):
    square = Square(side_a)
    assert square.side_a == side_a


@pytest.mark.parametrize("side_a", [0, -1])
def test_square_initialization_invalid(side_a):
    with pytest.raises(
        ValueError, match="Square sides can't be less than or equal to 0"
    ):
        Square(side_a)


@pytest.mark.parametrize(
    "side_a, expected_area",
    [
        (5, 25),
        (3, 9),
        (7, 49),
    ],
)
def test_square_get_area(side_a, expected_area):
    square = Square(side_a)
    assert square.get_area() == expected_area


@pytest.mark.parametrize(
    "side_a, expected_perimeter",
    [
        (5, 20),
        (3, 12),
        (7, 28),
    ],
)
def test_square_get_perimeter(side_a, expected_perimeter):
    square = Square(side_a)
    assert square.get_perimeter() == expected_perimeter
