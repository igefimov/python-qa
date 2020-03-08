from dz6a.source.Quadrilateral import Quadrilateral


class Square(Quadrilateral):
    def __init__(self, name, length):
        super().__init__(name, self.__class__.__name__, length, length)
