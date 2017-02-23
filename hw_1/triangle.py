
class Triangle:
    def __init__(self, point1, point2, point3):
        """
        :param point1: tuple<int>
        :param point2: tuple<int>
        :param point3:  tuple<int>
        """
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.edge12 = ((self.point1[1] - self.point2[1])**2 + (self.point1[1] - self.point2[1])**2)**0.5
        self.edge23 = ((self.point2[1] - self.point3[1]) ** 2 + (self.point2[1] - self.point3[1]) ** 2) ** 0.5
        self.edge31 = ((self.point3[1] - self.point1[1]) ** 2 + (self.point3[1] - self.point1[1]) ** 2) ** 0.5

    def is_triangle(self):
        """
        :return: bool
        """
        edges = sorted([self.edge12, self.edge23, self.edge31])
        return edges[0] + edges[1] > edges[2]

    def perimeter(self):
        """
        :return: int or float
        """
        return self.edge12 + self.edge23 + self.edge31

    def area(self):
        """
        :return: float
        """
        p = self.perimeter() / 2
        return (p * (p - edge12) * (p - edge23) * (p - edge31))**0.5
