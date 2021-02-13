"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares
desde 1 hasta ese número separados por comas.
"""
def run():
    numero = int(input("Ingresa un numero entero positivo: "))
    if numero <= 0:
        print("Error, porfavor ingresa un numero entero positivo")
    else:
        for i in range(numero):
            if (i % 2) != 0:
                print(f"{i}", end = ", ")
            else:
                continue
if __name__ == '__main__':
    run()