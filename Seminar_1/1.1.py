a = 123.6
b = -14
c = ['23', True]
d = ['abcdefg', 1]
s = 'ABCDEFG'
lista = ["qwe", False, 234.0, 'GHJK', float('-inf'), -1]

# 1. Ce vor afisa expresiile urmatoare si de ce?

print(b >= a and d < c)
# b >= a este False, deci 'False and ..' este intotdeauna False

print(b != a or 'abc' > s and len(s) == 4)
# prima data se executa "'abc' > s and len(s) == 4" si nu conteaza ce rezultat da deoarece b != a este True
# iar 'True or ..' este intotdeauna True