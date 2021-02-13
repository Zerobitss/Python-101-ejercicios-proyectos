"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
"""
def run():
    lista = []
    for i in range(1, 10 + 1):
        lista.append(i)
    print(lista)
    print(lista[::-1])
if __name__ == '__main__':
    run()