def insert_note(student, **kwargs):
    global catalog
    if student in catalog:
        if kwargs:
            for k in kwargs:
                if k in subjects_names:
                    if 0 <= kwargs[k] <= 10:
                        catalog[student][k].append(kwargs[k])
                    else:
                        print('The grade '+" "+ str(kwargs[k])+ 'is not a valid one.It has to be inserted between the gap of 0 and 10.')
                else:
                    print('The subject '+" "+ k +" "+ 'nu exista!')
        else:
            print('At least one grade must be asserted to the student!')
    else:
        print('The student'+" "+ student +" "+ ' nu este in catalog!')
subjects_names ={
    'g':'geography',
    'b':'biology',
    'p':'pedology'
}

catalog = {
    'Popescu Ion': {
        'g': [2, 5, 7],
        'b': [],
        'p': [6, 9, 8],
    },
    'Ionescu Geta': {
        'g': [6, 3, 8],
        'p': [4, 5],
        'b': [7, 9, 10]
    },
    'Georgescu Gelu': {
        'b': [2, 5, 7, 9],
        'g': [9, 8],
        'p': [6, 9]
    },
    'Radulescu Ioana': {
        'p': [7],
        'g': [6, 10, 9, 8],
        'b': [6, 9, 8],
    },
}
insert_note('Georgescu Gelu', b=10, g=7)
insert_note('Radulescu Ioana', p=9, b=7)
insert_note('Ionescu Geta', p=6)
insert_note('Popescu Ion', b=5)

print(catalog['Ionescu Geta'])
print(catalog['Radulescu Ioana'])
print(catalog['Ionescu Geta'])
print(catalog['Popescu Ion'])