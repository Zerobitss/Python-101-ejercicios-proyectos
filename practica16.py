"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe
mostrar un error.
"""
def divisor (num1, num2):
    result = num1 / num2
    print(f"Su resultado fue: {result}")
    return result
def run ():
    num1 = int(input("Ingresa numero: "))
    num2 = int(input("Ingresa divisor: "))
    if num2 == 0:
        print("Error no puede didivir entre 0")
    else:
        divisor(num1, num2)
if __name__ == '__main__':
    run()