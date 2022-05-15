def evaluation_media(t):
    if len(t) == 0:
        return 0
    return round(sum(t) / len(t), 2)

media =[]

catalog = {
    'Popescu Ion': [2, 5, 7],
    'Ionescu Geta': [10, 7, 9, 7],
    'Georgescu Gelu': [4, 2],
    'Radulescu Ioana': [5, 9, 6, 4, 10]
}
for s in catalog:
    media.append(evaluation_media(catalog[s]))
    print("The student's media"+ ' '+ s +' ' + "este"+ ' '+ str(media[-1]))

general_media = evaluation_media(media)
print("The general media of the class is: " + str(general_media))