from abc import ABC, abstractmethod
from math import sqrt, pi as PI


class Figure(ABC):

    __name = None
    __type = None
    __angles = None

    def __init__(self, name, figure_type, angles_count):
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

    def add_square(self, other):
        if isinstance(other, Figure):
            return self.area + other.area
        else:
            raise TypeError("We can add only square of two Figures!")


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


class Quadrilateral(Figure):

    __height = None
    __width = None

    def __init__(self, name, figure_type, height, width):
        if type(self) is Quadrilateral:
            raise NotImplementedError("We cannot instantiate this class!")
        super().__init__(name, figure_type, 4)
        self.__height = height
        self.__width = width

    @property
    def area(self):
        return self.__height * self.__width

    @property
    def perimeter(self):
        return 2 * self.__height + 2 * self.__width


class Rectangle(Quadrilateral):
    def __init__(self, name, height, width):
        super().__init__(name, self.__class__.__name__, height, width)


class Square(Quadrilateral):
    def __init__(self, name, length):
        super().__init__(name, self.__class__.__name__, length, length)


if __name__ == "__main__":
    # circle1 = Circle("треугольник1", 15)
    # print(circle1.get_name() + ":")
    # print(circle1.area)
    # print(circle1.perimeter)
    #
    circle2 = Circle("круг", 20)
    print(circle2)

    # print(circle1.add_square(circle2))
    #
    #
    # print(circle2.get_type())
    #
    # print(circle2)

    r = Rectangle("quad1", 10, 20)
    print(r)

    print("Area sum of two previous figures is: {0}".format(r.add_square(circle2)))

    square1 = Square("square1", 10)
    print(square1)

    triangle1 = Triangle("tr1", 10, 20, 30)
    print(triangle1)
