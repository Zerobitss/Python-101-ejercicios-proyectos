"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero
separados por comas.
"""
def run():
    numero = int(input("Ingresa un numero entero positivo: "))
    if numero <= 0:
        print(f"Error, el numero {numero} tiene que ser positivo y mayor a 0")
    else:
        for i in range(numero, -1, -1):
            print(f"Numeros: {i}", end=", ")
if __name__ == '__main__':
    run()