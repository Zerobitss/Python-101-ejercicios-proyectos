"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los
muestre por pantalla ordenados de menor a mayor.
"""
def run():
    loteria = []
    for i in range(5):
        numeros = int(input("Ingresa los numeros ganadores: "))
        loteria.append(numeros)
    loteria.sort()
    print(f"Los numeros ganadores de menor a mayor son: {loteria}")
if __name__ == '__main__':
    print("Bienvenido a la loteria primitiva")
    run()