import math

class Polygon:
    def __init__(self, nbrsides):
        self.nbr_sides = nbrsides

    def whoamI(self):
        polygons = [None, None, None, "Triangle", "Rectangle", "Pentagon", "Hexagon", "Septagon", "Octagon", "Nonagon", "Decagon"]
        for n in range(3, 11):
            if self.nbr_sides == n:
                return polygons[n]
       
    def howmanysides(self):
        return self.nbr_sides

    def area(self):
        return "No Area"

    def perimeter(self):
        return "No Perimeter"


class Triangle(Polygon):
    def __init__(self, a, b, c):
        Polygon.__init__(self, 3)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * ((s - self.a) * (s - self.b) * (s - self.c)))
        return area

    def perimeter(self):
        return self.a + self.b + self.c


class Rectangle(Polygon):
    def __init__(self, breadth, length):
        Polygon.__init__(self, 4)
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


if __name__ == '__main__':
    tri1 = Triangle(2, 2, 2)
    rect = Rectangle(2, 3)
    tri2 = Triangle(3, 3, 3)
    figures = [tri1, rect, tri2]
    for fig in figures:
        print("Type of Polygon =>", fig.whoamI())
        print("Sides =", fig.howmanysides())
        print("Area =", fig.area())
        print("Perimeter =", fig.perimeter())
