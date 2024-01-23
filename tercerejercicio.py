import csv

with open('juegos.csv') as file:
    csv_reader = csv.reader(file, delimiter=';')
    next(csv_reader)

    for row in csv_reader:
        juego = row[0]
        precio = row[1]
        genero = row[2]
        print('----------------')
        print('Juego: ', juego)
        print('Precio: ', precio)
        print('Genero: ', genero)