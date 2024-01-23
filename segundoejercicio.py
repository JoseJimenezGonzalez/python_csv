import csv

with open('juegos.csv') as file:
    csv_reader = csv.reader(file, delimiter=';')

    for row in csv_reader:
        juego, precio, genero = row
        print(juego, precio, genero)