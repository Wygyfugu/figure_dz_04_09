from src.rectangle import Rectangle
import pytest

def test_rectangle_area_positive():
    a = 3
    b = 5
    a += 1
    b += 1
    r = Rectangle(a, b)
    assert r.get_area == 24, f'Area should be 15'
    a -= 1
    b -= 1
    print(a)
    print(b)
@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        pytest.param(3, 5, 15, marks=pytest.mark.skip),
        (3.5, 5.5, 19.25)
    ],
    ids=["integer", "float"]
)
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area == area, f"Area should be {area}"
