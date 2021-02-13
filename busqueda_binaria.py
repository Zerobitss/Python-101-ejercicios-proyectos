import random
#Generar un contador de cuantas veces estamos buscando, cuantas veces estamos iterando dentro de los algoritmos
#Mostrar como va creciendo el tiempo de busqueda, es decir cuantos tardamos adicinonales o a comparacion con el otro
counter = 0
def busqueda_binaria(lista, comienzo, final, objetivo):
    global counter
    counter += 1

    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        counter = len(lista)
        return False

    #Dividir la lista en dos
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, comienzo, medio -1, objetivo)

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

def run_lineal():
    print("BUSQUEDA LINEAL")
    tamano_lista = int(input("De que tamaño sera tu lista: "))
    objetivo = int(input("Que numero quieres encontrar: "))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print(lista)
    encontrado = busqueda_lineal(lista, objetivo)
    print(f'El elemento {objetivo}  {"Esta" if encontrado else "no esta"} en la lista')

def run_binaria():
    print("BUSQUEDA BINARIA")
    tamano_lista = int(input("De que tamaño sera tu lista: "))
    objetivo = int(input("Que numero quieres encontrar: "))
    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    print(lista)
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(f'El elemento {objetivo}  {"Esta" if encontrado else "no esta"}')
    print(f"Pasos: {counter}")


if __name__ == "__main__":
    run_lineal()
    run_binaria()