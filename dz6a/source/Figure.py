from abc import abstractmethod


class Figure:

    _name = None
    _type = None
    __angles = None

    def __init__(self, name, figure_type, angles_count):
        if type(self) is Figure:
            raise NotImplementedError("We cannot instantiate this class!")
        self._name = name
        self._type = figure_type
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
        return "<--\nFigure Name: {0}\nFigure Type: {1}\nFigure Square: {2}\nFigure Perimeter: {3}\nFigure has {4} angels\n-->"\
            .format(self._name, self._type, format(self.area, '.3f'), format(self.perimeter, '.3f'), self.__angles)

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_angels(self):
        return self.__angles

    def add_area(self, other):
        if isinstance(other, Figure):
            return self.area + other.area
        else:
            raise TypeError("We can add only square of two Figures!")
