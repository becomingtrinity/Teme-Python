class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_distance(self):
        return round((self.a ** 2 + self.b ** 2) ** 0.5, 2)
a = float(input('The value of a is: '))
b = float(input('The value of b is: '))

P = Point(a, b)
print('The distance from the point to the origin is: ', P.get_distance())
