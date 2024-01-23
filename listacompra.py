import csv
import os

def mostrar_menu():
    print("==== Lista de la Compra ====")
    print("1. Introducir producto a la lista")
    print("2. Leer la lista")
    print("3. Borrar la lista")
    print("4. Pasar a csv la lista")
    print("5. Salir")

def introducir_productos():
    productos = input("Introduce el producto: ")
    with open("lista_compra.txt", "a") as archivo:
        archivo.write(productos + "\n")
    print("Producto añadido a la lista.")

def leer_lista():
    try:
        with open("lista_compra.txt", "r") as archivo:
            lista = archivo.read()
            if lista:
                print("Lista de la compra:")
                print(lista)
            else:
                print("La lista de la compra está vacía.")
    except FileNotFoundError:
        print("La lista de la compra está vacía.")

def borrar_lista():
    try:
        os.remove("lista_compra.txt")
        print("Lista de la compra borrada.")
    except FileNotFoundError:
        print("La lista de la compra ya está vacía.")


def pasar_lista_compra_a_csv():

    columnas = ['Lista de la compra']

    try:
        with open("lista_compra.txt", "r") as archivo:
            lista = archivo.read()

            with open('lista_compra.csv', mode='w') as file:
                writer = csv.DictWriter(file, delimiter=' ', fieldnames=columnas)
                writer.writeheader()


    except FileNotFoundError:
        print("La lista de la compra está vacía.")


def main():


    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            introducir_productos()
        elif opcion == "2":
            leer_lista()
        elif opcion == "3":
            borrar_lista()
        elif opcion == "4":
            pasar_lista_compra_a_csv()
        elif opcion == "5":
            print("Saliendo de la aplicación. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1-5).")



if __name__ == "__main__":
    main()
