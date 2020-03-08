from math import sqrt
from dz6a.source.Figure import Figure


class Triangle(Figure):
    __lateralA = None
    __lateralB = None
    __lateralC = None

    def __init__(self, name, lateral1, lateral2, lateral3):
        super().__init__(name, self.__class__.__name__, 3)
        self.__lateralA, self.__lateralB, self.__lateralC = lateral1, lateral2, lateral3

    @property
    def area(self):
        p = self.perimeter
        return sqrt(p * (p - self.__lateralA) * (p - self.__lateralB) * (p - self.__lateralC))

    @property
    def perimeter(self):
        return self.__lateralA + self.__lateralB + self.__lateralC

