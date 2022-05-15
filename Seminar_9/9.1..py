def non_lambda(tuple):
    return tuple[0] * tuple[1]
l = [(5, 21), (6, 11), (0, 25), (-6, 6)]

print(sorted(l, key=non_lambda))
print(sorted(l, key=lambda tuple: tuple[0] * tuple[1]))