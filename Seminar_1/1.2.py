a = 123.6
b = -14
c = ['23', True]
d = ['abcdefg', 1]
s = 'ABCDEFG'
lista = ["qwe", False, 234.0, 'GHJK', float('-inf'), -1]

print(not (b >= a and d < c))
# datorita parantezelor prima data not se aplica la toata expresia (b >= a and d < c) care este False, deci negata este True
print(not b >= a and d < c)
# a doua oara not se aplica doar la b >= a, care este False deci negata este True, iar d < c este de asemenea True, deci intreaga expresie este True