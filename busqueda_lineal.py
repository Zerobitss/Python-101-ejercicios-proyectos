import random

#esto que se aplica aqui es: O(1)

def busqueda_lineal(lista, objetivo):
    match = False
    counter = 0

    for elemento in lista: #O(n)
        counter +=1
        if elemento == objetivo:
            match = True
            break

    print(f"Numero de pasos: {counter}")
    return match

def run():
    tamano_lista = int(input("De que tamaño sera tu lista: "))
    objetivo = int(input("Que numero quieres encontrar: "))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print(lista)
    encontrado = busqueda_lineal(lista, objetivo)
    print(f'El elemento {objetivo}  {"Esta" if encontrado else "no esta"} en la lista')

if __name__ == "__main__":
    run()