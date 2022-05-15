def media(t):
    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)


def get_maxim_numbers(c, h1, h2):
    max_name = len(h1)
    max_surname = len(h2)
    for k in c:
        name, surname = k.split()
        if len(name) > max_name:
            max_name = len(name)
        if len(surname) > max_surname:
            max_surname = len(surname)
    return max_name, max_surname


catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

m, d = 5, 2
h1 = "The name"
h2 = "The surname"
n, p = get_maxim_numbers(catalog, h1, h2)
h = f'| {h1:{n}} {h2:{p}} {"Media":{m}} {"Grades":>{m}} |'

print('-' * len(h))
print(h)
print('-' * len(h))

for student in sorted(catalog):
    name, surname = student.split()
    print(f'| {name:<{n}} {surname:<{p}} {media(catalog[student]):>{m}.{d}f} {len(catalog[student]):^{m}} |')

print('-' * len(h))