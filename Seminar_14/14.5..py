from modul.geome import Point, Rectangle

r_angle_1 = Rectangle(Point(4, 6), Point(2, 9))
r_angle_2 = Rectangle(Point(-4, -6), Point(-2,-9))
r_angle_3 = Rectangle(Point(9, 10), Point(7, 11))
r_angle_4 = Rectangle(Point(-9, -6), Point(-7, -11))

print(Rectangle.instances, Rectangle.square_instances, Rectangle.squares_percent())


