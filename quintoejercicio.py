import csv

cursos = [
    {
         'id': 1,
         'titulo': 'Curso profesional de Python',
         'descripcion': 'Descripcion 1'
    } ,
    {
          'id': 2,
          'titulo': 'Curso profesional de Django',
          'descripcion': 'Descripcion 2'
    } ,
    {
        'id': 3,
        'titulo': 'Curso profesional de Base de datos',
        'descripcion': 'Descripcion 3'
    } ,
]

columnas = ['id', 'titulo', 'descripcion']

with open('cursos.csv', mode='w') as file:
    writer = csv.DictWriter(file, delimiter=';', fieldnames=columnas)
    writer.writeheader()

    for curso in cursos:
        writer.writerow(curso)

