a = float(input('Lungimea laturii a: '))
b = float(input('Lungimea laturii b: '))
c = float(input('Lungimea laturii c: '))

dreptunghic = (round (b * b) == a * a + c * c) or (round (a * a) == b * b + c * c) or (round(c * c) == a * a + b * b)
echilateral = (a == b == c)
isoscel = (a == b or b == c or c == a)

if echilateral:
    print('Triunghiul este echilateral')
elif isoscel:
    if dreptunghic:
        print('Triunghiul este isoscel si dreptunghic')
    else:
        print('Triunghiul este isoscel')
elif dreptunghic:
    print('Triunghiul este dreptunghic')
else:
    print('Triunghiul este oarecare')