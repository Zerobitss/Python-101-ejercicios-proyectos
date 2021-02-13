import random

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
def run():
    tamano_lista = int(input("De que tamaño sera tu lista: "))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print(lista)
    lista_ordenada = ordenamiento_burbuja(lista)
    print(lista_ordenada)

if __name__ == "__main__":
    run()
