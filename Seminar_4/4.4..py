def median(tuple):
    if len(tuple) == 0:
        return 0
    aritmethic= 0
    for e in tuple:
        aritmethic += e
    return aritmethic / len(tuple)


evaluations = (8, 5, 10, 6, 9)
print('The evaluation media is: ', median(evaluations))