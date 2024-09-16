import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize("side_a, side_b", [(3, 5)])
def test_rectangle_initialization_valid(side_a, side_b):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.side_a == side_a
    assert rectangle.side_b == side_b


@pytest.mark.parametrize("side_a, side_b", [(0, 5), (3, 0), (-1, 5), (3, -1)])
def test_rectangle_initialization_invalid(side_a, side_b):
    with pytest.raises(
        ValueError, match="Rectangle sides can't be less than or equal to 0"
    ):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    "side_a, side_b, expected_area",
    [
        (3, 5, 15),
        (2, 4, 8),
        (7, 8, 56),
    ],
)
def test_rectangle_get_area(side_a, side_b, expected_area):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.get_area() == expected_area


@pytest.mark.parametrize(
    "side_a, side_b, expected_perimeter",
    [
        (3, 5, 16),
        (2, 4, 12),
        (7, 8, 30),
    ],
)
def test_rectangle_get_perimeter(side_a, side_b, expected_perimeter):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.get_perimeter() == expected_perimeter
