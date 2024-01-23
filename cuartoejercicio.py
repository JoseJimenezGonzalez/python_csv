import csv

with open('juegos.csv') as file:
    csv_reader = csv.DictReader(file, delimiter=';')

    for row in csv_reader:
        juego = row['Juego']
        precio = row['Precio']
        genero = row['Genero']
        print('----------------')
        print('Juego: ', juego)
        print('Precio: ', precio)
        print('Genero: ', genero)