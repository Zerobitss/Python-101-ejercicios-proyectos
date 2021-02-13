"""
Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial
y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla
con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
"""
"""
calculadora, seno coseno tangete
import math
s = input("Escribe un numero: ") #Captura un numero
s1 = float (s) #Transforma a flotante
s2 = math.radians(s1) #Transforma a radianes

x = math.radians()
y = math.radians()
z = math.radians()
a = math.exp() # Calculo exponencial
b = math.log() #Logaritmo neperiano

print(math.sin(s2))
print(math.sin(x))
print(math.cos(y))
print(math.tan(z))
"""
import math
def calculadora_cientifica(numero):
    for i in range(1, numero + 1):
        if i % 2 == 0:
            print(f"Numeros pares: {i}")
    opcion = int(input("""
    1.- Seno
    2.- Coseno
    3.- Tangente
    4.- Exponencial
    5.- Logaritmo neperiano

    Que tipo de calculo deseas realizar: """))
    for j in range(1, numero+ 1):
        calculos(opcion, j)
def calculos(opcion, valor):
    if opcion == 1:
        valor = math.radians(valor)
        print("Calculo de Seno", end=" ")
        return print(math.sin(valor))
    elif opcion == 2:
        valor = math.radians(valor)
        print("Calculo de Coseno", end=" ")
        return print(math.cos(valor))
    elif opcion == 3:
        valor = math.radians(valor)
        print("Calculo de Tangente", end = " ")
        return print(math.tan(valor))
    elif opcion == 4:
        print("Calculo Exponencial")
        return print(math.exp(valor))
    elif opcion == 5:
        print("Calculo Logaritmo natural")
        return print(math.log(valor))
    else:
        print("Opcion incorrecta")
def run():
    print("Calculadora cientifica")
    numero = int(input("Ingresa un numero: "))
    calculadora_cientifica(numero)
if __name__ == "__main__":
    run()