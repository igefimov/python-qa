from math import pi as PI

from dz6a.source.Figure import Figure


class Circle(Figure):

    __radius = None

    def __init__(self, name, radius):
        super().__init__(name, self.__class__.__name__, 0)
        self.__radius = radius

    def __str__(self):
        return "<--\nFigure Name: {0}\nFigure Type: {1}\nFigure Square: {2}\nFigure Perimeter: {3}\n-->"\
                .format(self._name, self._type, format(self.area, '.3f'), format(self.perimeter, '.3f'))

    @property
    def perimeter(self):
        return 2 * PI * self.__radius

    @property
    def area(self):
        return PI * self.__radius * self.__radius
