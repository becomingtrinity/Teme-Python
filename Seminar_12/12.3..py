from module.geometry import Point

a1 = float(input('The value of a1:'))
b1 = float(input('The value of b1:'))

a2 = float(input('The value of a2: '))
b2 = float(input('The value of b2: '))

P1 = Point(a1, b1)
P2 = Point(a2, b2)

if P1.get_distance() < P2.get_distance():
    print('P2 is way farer from the center than P1')
elif P1.get_distance() > P2.get_distance():
    print('P1 is way farer from the center than P2')
else:
    print('The points are at equal distance from the center')