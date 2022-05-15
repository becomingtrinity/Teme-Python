def student_data(student, note):
    global catalog
    if student in catalog:
        if 0 <= note <= 10:
            catalog[student].append(note)
        else:
            print('Your note' + str(note) + 'is not evaluable.It must be evaluated between 1 and 10')
    else:
        print('The student' + student + 'is not introduced in the catalog')

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}

student_data('Radulescu Ioana', 8)
student_data('Ionescu Geta', 6)
student_data('Georgescu Gelu', 10)
student_data('Popescu Ion', 9)

print(catalog)