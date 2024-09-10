from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrise(
    "side_a, side_b, area",
    [
        (3, 5, 15),
        (3.5, 5.5, 19.25)
    ]
)
def test_rectangle_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area, f"Area should be {area}"
