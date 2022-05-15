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
evaluation_list = []
for student, students_grades in list(students_grades.items()):
    evaluation_list.append((evaluation_media(students_grades), student))
for evaluation_media, student in sorted(evaluation_list, reverse = True):
    print(student, evaluation_media)