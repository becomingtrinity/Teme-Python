def erase_note(student, note=None):
    global catalog
    if student in catalog:
        if note is None:
            catalog[student].clear()
        else:
            if note in catalog[student]:
                catalog[student].remove(note)
            else:
                print('The student evaluated' + student + 'does not have any grade of' + str(note) + '!')
    else:
        print('The student' +student+ 'has not been found in the catalog')

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

erase_note('Radulescu Ioana', 4)
erase_note('Ionescu Geta', 7)
erase_note('Georgescu Gelu', 2)
erase_note('Popescu Ion', 5)

print(catalog)

