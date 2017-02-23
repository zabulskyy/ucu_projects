
class Point:
    def __init__(self, x=0, y=0):
        """
        :param x: int
        :param y: int
        """
        self.move(x, y)

    def move(self, x, y):
        """
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y

    def rotate(self, beta, other_point):
        """
        :param beta: int
        :param other_point: int
        :return: None
        """
        from math import radians
        dx = self.x - other_point.get_xposition()
        dy = self.y - other_point.get_yposition()
        beta = radians(beta)
        xpoint3 = dx * cos(beta) - dy * sin(beta)
        ypoint3 = dy * cos(beta) + dx * sin(beta)
        xpoint3 = xpoint3 + other_point.get_xposition()
        ypoint3 = ypoint3 + other_point.get_yposition()
        return self.move(xpoint3, ypoint3)

    def get_xposition(self):
        """
        :return: int or float
        """
        return self.x

    def get_yposition(self):
        """
        :return: int or float
        """
        return self.y

    def __add__(self, other):
        """
        :return: int or float
        """
        return Point(self.get_xposition() + other.get_xposition(), self.get_yposition() + other.get_yposition())

    def __iadd__(self, other):
        """
        :return: int or float
        """
        return Point(self.get_xposition() + other.get_xposition(), self.get_yposition() + other.get_yposition())

    def __sub__(self, other):
        """
        :return: int or float
        """
        return Point(self.get_xposition() - other.get_xposition(), self.get_yposition() - other.get_yposition())

    def __isub__(self, other):
        """
        :return: int or float
        """
        return Point(self.get_xposition() - other.get_xposition(), self.get_yposition() - other.get_yposition())

    def __mul__(self, other):
        """
        :return: int or float
        """
        return Point(self.get_xposition() * other.get_xposition(), self.get_yposition() * other.get_yposition())

    def __imul__(self, other):
        """
        :return: int or float
        """
        return Point(self.get_xposition() * other.get_xposition(), self.get_yposition() * other.get_yposition())

    def __truediv__(self, other):
        """
        :return: int or float
        """
        return Point(self.get_xposition() / other.get_xposition(), self.get_yposition() / other.get_yposition())

    def __itruediv__(self, other):
        """
        :return: int or float
        """
        return Point(self.get_xposition() / other.get_xposition(), self.get_yposition() / other.get_yposition())

    def __floordiv__(self, other):
        """
        :return: int
        """
        return Point(self.get_xposition() // other.get_xposition(), self.get_yposition() // other.get_yposition())

    def __ifloordiv__(self, other):
        """
        :return: int
        """
        return Point(self.get_xposition() // other.get_xposition(), self.get_yposition() // other.get_yposition())

