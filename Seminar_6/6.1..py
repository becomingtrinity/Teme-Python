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
n, m, d = 32, 5, 2
print(f'{"Name":{m}} {"Media":{n}}')
print("-" * (m + n + 1))

for student in catalog:
    mid = media(catalog[student])
    print(f'{student:<{n}} {mid:>{m}.{d}f}')