import csv

with open('juegos.csv') as file:
    csv_reader = csv.reader(file, delimiter=';')
    next(csv_reader)

    for row in csv_reader:
        print(row)
