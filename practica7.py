"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa
debe mostrar un error.
"""
def run():
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    result = num1 / num2
    if result == 0:
        print("Error!")
    else:
        print(f"El resultado es: {result}")
if __name__ == '__main__':
    run()