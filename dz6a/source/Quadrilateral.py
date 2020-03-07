from dz6a.source.Figure import Figure


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
