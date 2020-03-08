import pytest

from source.Figure import Circle, Figure, Quadrilateral, Rectangle, Square, Triangle


def test_01_figure():
    with pytest.raises(NotImplementedError):
        Figure("name1", "Quadrilateral", 30)


def test_02_quadrilateral():
    with pytest.raises(NotImplementedError):
        Quadrilateral("name1", "Quadrilateral", 30, 40)


def test_03_rectangle_area():
    rectangle1 = Rectangle("rec1", 10, 20)
    assert rectangle1.area == 200


def test_04_triangle_perimeter():
    assert Triangle("tr1", 5, 10, 15).perimeter == 30


def test_05_circle_area_vs_perimeter():
    circle1 = Circle("circle1", 10)
    assert circle1.area > circle1.perimeter
    circle1 = Circle("circle1", 0.5)
    assert circle1.area < circle1.perimeter


def test_06_add_area():
    square1 = Square("square1", 10)
    rectangle1 = Rectangle("rectangle1", 5, 10)
    assert square1.add_area(rectangle1) == 150
