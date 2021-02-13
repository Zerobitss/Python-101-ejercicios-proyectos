"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
def run():
    print("🤗Bienvenido al programa para saber si eres mayor o no 😁")
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print("Si eres mayor de edad")
    else:
        print("No eres mayor de edad")
if __name__ == '__main__':
    run()
