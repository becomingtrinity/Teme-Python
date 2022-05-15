def evaluation_media(t):
    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)

students_grades = {
    'Popescu Ion': (2, 5, 7),
    'Ionescu Geta': (10, 7, 9, 7),
    'Georgescu Gelu': (4, 2),
    'Radulescu Ioana': (5, 9, 6, 4, 10)
}

corrigent_student = {}
for student in students_grades:
    evaluation_list = evaluation_media(students_grades[student])
    if evaluation_list < 5:
        corrigent_student[student] = evaluation_list

print(corrigent_student)