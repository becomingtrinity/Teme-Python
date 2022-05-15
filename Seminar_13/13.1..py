from Seminar_12.module.geometry import Point, Rectangle
x1 = float(input('Insert the coordinate x of p1:'))
y1 = float(input('Insert the coordinate y of p1:'))
x2 = float(input('Insert the coordinate x of p2:'))
y2 = float(input('Insert the coordinate y of p2:'))

r = Rectangle(Point(x1, y1), Point(x2, y2))

print('The dimensions of the sides are: ', r.get_dimensions())
print('The area is: ', r.get_area())
print('The perimeter is: ', r.get_perimeter())