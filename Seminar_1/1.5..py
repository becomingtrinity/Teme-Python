a = 123.6
b = -14
c = ['23', True]
d = ['abcdefg', 1]
s = 'ABCDEFG'
lista = ["qwe", False, 234.0, 'GHJK', float('-inf'), -1]

n = input('Introdu un numar: ')
print('Numarul ridicat la patrat este: ', n ** 2)
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# Ne da eroare fiindca noi am introdus un tip string, iar programul asteptase un input de tip integer

