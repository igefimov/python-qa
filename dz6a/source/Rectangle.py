from dz6a.source.Quadrilateral import Quadrilateral


class Rectangle(Quadrilateral):
    def __init__(self, name, height, width):
        super().__init__(name, self.__class__.__name__, height, width)
