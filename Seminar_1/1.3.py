a = 123.6
b = -14
c = ['23', True]
d = ['abcdefg', 1]
s = 'ABCDEFG'
lista = ["qwe", False, 234.0, 'GHJK', float('-inf'), -1]

8 / 2 * 'abc'
# 8 / 2 returneaza un numar float (4.0) care nu se poate inmulti cu un string

8 // 3 * [3, 'def']
# e ok, 8 // 3 returneaza un intreg (2) si acesta se poate inmulti cu o lista

d >= s
# eroarea afisata spune totul: TypeError: '>=' not supported between instances of 'list' and 'str'

[s] <= c
# e ok, se compara doua liste

s <= c
# din nou eroare sugestiva: TypeError: '<=' not supported between instances of 'str' and 'list'

s <= c[0]
# e ok, se compara doua stringuri

s <= c[2/2]
# 2/2 este un float. De aici si eroarea: TypeError: list indices must be integers or slices, not float

s <= c[6]
# nu avem indexul 6 in c. De aici eroarea: IndexError: list index out of range