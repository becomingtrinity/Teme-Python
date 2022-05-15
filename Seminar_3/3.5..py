s = "În livada noastra avem ciresi, meri, peri și pruni. " \
    "Care fructe credeti ca se coc primele? " \
    "Variante: perele, merele, prunele și apoi ciresele. " \
    "Foarte gresit! " \
    "Corect este: ciresele, merele, perele și apoi prunele."

nr_propozitii = s.count('.') + s.count('!') + s.count('?')

print('Numar propozitii:', nr_propozitii)

cuvinte = s.split()
for i in range(len(cuvinte)):
    cuvinte[i] = cuvinte[i].lower().strip(',?!:.')

print('Numarul de cuvinte este:', len(cuvinte))
print('Cuvintele sunt:', cuvinte)