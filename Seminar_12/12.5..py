from module.geometry import Point, Circle

def view_dist(p):
    for i in p:
        print(i.get_distance())

def get_dist(i):
    return i.get_distance()
p1 = Point(4, 8.5)
p2 = Point(3, 4)
p3 = Point(-5, 6)
c = Circle(-100, 100, 2)
l = [c, p1, p2, p3]
view_dist(l)

print('----------------')

lI = sorted(l, key=get_dist)
view_dist(lI)

print('----------------')

lII = sorted(l, key=Point.get_distance)
view_dist(lII)

print('----------------')

lIII = sorted(l, key=lambda p: p.get_distance())
view_dist(lIII)