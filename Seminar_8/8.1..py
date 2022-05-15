# a.
ls = ['5', '123', '-7', '33']
li = [5, 123, -7, 33]

print(sorted(ls))
print(sorted(ls, key=int))
# b.
def add_all(t: tuple) -> int:
    return t[0] + t[1]


l = [(5, 21), (6, 11), (0, 25), (-6, 6)]

print(sorted(l))
print(sorted(l, key=add_all))
print(sorted(l, key=sum))