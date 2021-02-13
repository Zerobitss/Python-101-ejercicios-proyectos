"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
def run():
    numero = int(input("Escribe un numero entero: "))
    if numero % 2 == 0:
        print("Es un numero par")
    else:
        print("Es un numero impar")
if __name__ == '__main__':
    run()