def media(t):
    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

n, m, d = 25, 5, 2
h = f'| {"Name":{n}} {"Surname":{n}} {"Media":{m}} {"Grades":>{m}} |'

print('-' * len(h))
print(h)
print('-' * len(h))

for student, grades in catalog.items():
    name, surname = student.split()
    print(f'| {name:<{n}} {surname:<{n}} {media(grades):>{m}.{d}f} {len(grades):^{m}} |')

print('-' * len(h))