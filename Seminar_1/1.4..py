a = 123.6
b = -14
c = ['23', True]
d = ['abcdefg', 1]
s = 'ABCDEFG'
lista = ["qwe", False, 234.0, 'GHJK', float('-inf'), -1]

print("GHJK" not in lista)
# "GHJK" este in lista, asadar operatorul not in va returna False

print(234 in lista)
# 234 este in lista

print((a < b) in lista)
# a < b este False. False este in lista. Deci rezultatul final este True

print(lista[len(lista) - 1] * lista[2] > 0)
# len(lista) - 1 este 5, lista[5] este -1, lista[2] este 234.0, -1 * 234.0 este -234.0, -234.0 > 0 este False