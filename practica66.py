"""
4: Crea una variable y asignale un valor entero. Pidele al usuario un numero por teclado, crea una variable usuario,
a la misma variable asignale una multiplicacion por 9.
Luego multiplica en asignacion la primer variable con la segunda e imprime
en pantalla el resultado.
"""
def run ():
    entero = 5
    numero = int(input("Ingresa un numero entero: "))
    numero *= 9
    result = numero * entero
    print(result)
if __name__ == "__main__":
    run()