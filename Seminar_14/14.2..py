from modul.geome import Point, Rectangle

rectangle_1 = Rectangle(Point(3, 9), Point(6, 14))
rectangle_2 = Rectangle(Point(7, 11), Point(10, 19))

print(rectangle_1.is_square())
print(rectangle_2.is_square())