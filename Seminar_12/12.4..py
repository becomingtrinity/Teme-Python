from module.geometry import Circle
x = float(input('The value of x is: '))
y = float(input('The value of y is: '))
r = float(input('The value of r is: '))

circle = Circle(x, y, r)

Distance = print('The distance from the circle to the center is: ', circle.get_distance())
Area = print('The area of the given circle is: ', circle.get_area())
