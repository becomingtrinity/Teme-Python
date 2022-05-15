def evaluation_media(t):
    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)

def arithmetic_media(student, subject=None):
    global catalog
    for geography in catalog[student]:
        if subject is None:
            print('Student'+ ' '+ student + ' '+ "has the following grades: ")
            for geography in catalog[student]:
                print("The student's grade at subject"+' '+ subjects_names[geography] + " is " + str(evaluation_media(catalog[student][geography])))
        else:
            if subject in subjects_names:
                s = evaluation_media(catalog[student][subject])
                print('The media of student '+ " "+ student +" "+ ' at subject '+" "+ subjects_names[subject] + ' is ' + str(s))
            else:
                print('The subject does not exist')
    else:
            print(' The student ' + student + ' is not in the catalog!')

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
for s in catalog:
    arithmetic_media(s, 'g')

arithmetic_media('Radulescu Ioana')