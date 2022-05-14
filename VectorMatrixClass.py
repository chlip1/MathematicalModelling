
class Vector:  # definiowanie operatorow przeciazonych dla wektorow 2x1

    def __init__(self, a, b):
        self.data = [a, b]

    def __add__(self, other):
        if isinstance(other, Vector):  # dodawanie dwoch wektorow
            return Vector(self.data[0] + other.data[0],
                          self.data[1] + other.data[1])
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):  # mnozenie wektor razy skalar
            return Vector(self.data[0] * other,
                          self.data[1] * other)

        if isinstance(other, Vector):        # mnozenie wektor razy wektor
            return float(self.data[0] * other.data[0] + self.data[1] * other.data[1])

        else:
            return NotImplemented


class Matrix:   # definiowanie operatorow przeciazonych dla macierzy 2x2

    def __init__(self, a, b, c, d):
        self.data = [[a, b],
                     [c, d]]

    def __mul__(self, other):
        if isinstance(other, Vector):         # mnozenie macierz razy wektor
            return Vector(self.data[0][0] * other.data[0] + self.data[0][1] * other.data[1],
                          self.data[1][0] * other.data[0] + self.data[1][1] * other.data[1])
        else:
            return NotImplemented
