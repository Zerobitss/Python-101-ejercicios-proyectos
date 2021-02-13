"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra
introducida empezando por la última.
"""
def run():
    lista = []
    word = str(input("Ingresa una palabra: "))
    lista.append(word)
    for i in word:
        reversa = word[::-1]
    print(reversa)
if __name__ == '__main__':
    run()