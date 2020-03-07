from abc import abstractmethod
from dz6a.source.Circle import Circle


class Figure:

    __name = None
    __type = None
    __angles = None

    def __init__(self, name, figure_type, angles_count):
        if type(self) is Figure:
            raise NotImplementedError("We cannot instantiate this class!")
        self.__name = name
        self.__type = figure_type
        self.__angles = angles_count

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        if isinstance(self, Circle):
            return "<--\nFigure Name: {0}\nFigure Type: {1}\nFigure Square: {2}\nFigure Perimeter: {3}\n-->"\
                .format(self.__name, self.__type, format(self.area, '.3f'), format(self.perimeter, '.3f'))
        else:
            return "<--\nFigure Name: {0}\nFigure Type: {1}\nFigure Square: {2}\nFigure Perimeter: {3}\nFigure has {4} angels\n-->"\
                .format(self.__name, self.__type, format(self.area, '.3f'), format(self.perimeter, '.3f'), self.__angles)

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_angels(self):
        return self.__angles

    def add_area(self, other):
        if isinstance(other, Figure):
            return self.area + other.area
        else:
            raise TypeError("We can add only square of two Figures!")
