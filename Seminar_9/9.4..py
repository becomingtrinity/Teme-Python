premiers ={
    'Bengescu Hortensia': 9.16,
    'Vasilescu Vasile': 9.00,
    'Ionescu Geta': 8.34,
}
with open('input/diploma.txt', 'r') as file:
    diploma = file.read()
    for i, e in enumerate(sorted(premiers, key=premiers.get, reverse=True), start=1):
        with open(f'output/premiu-{i}.txt', 'w') as file:
            print(diploma.format(i * 'I', e, premiers[e]), file=file)

from docxtpl import DocxTemplate

premiers = {
    'Bengescu Hortensia': 9.16,
    'Vasilescu Vasile': 9.00,
    'Ionescu Geta': 8.34,
}

doc = DocxTemplate("input/diploma.docx")

for i, e in enumerate(sorted(premiers, key=premiers.get, reverse=True), start=1):
    context = {'e': e, 'p': i * 'I', 'm': premiers[e]}
    doc.render(context)
    doc.save(f'output/premiu-{i}.docx')


