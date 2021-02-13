"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
def run():
    num = int(input("Ingresa un numero entero: "))
    if num % 2 == 0:
        print(f"El numero es {num} es par")
    else:
        print(f"El numero {num} es impar")
if __name__ == '__main__':
    run()