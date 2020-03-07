from math import pi as PI

from dz6a.source.Figure import Figure


class Circle(Figure):

    __radius = None

    def __init__(self, name, radius):
        super().__init__(name, self.__class__.__name__, 0)
        self.__radius = radius

    @property
    def perimeter(self):
        return 2 * PI * self.__radius

    @property
    def area(self):
        return PI * self.__radius * self.__radius


# if __name__ == "__main__":
#     circle1 = Circle("треугольник1", 15)
#     print(circle1)
