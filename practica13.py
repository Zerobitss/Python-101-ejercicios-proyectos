"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio
que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""
def run():
    edad = int(input("Ingresa tu edad: "))
    if (edad < 4):
        print("Tu entrada es gratis")
    elif (edad > 4) and (edad < 18):
        print("Debbes pagar 5€")
    elif (edad > 18):
        print("Debes pagar 10€")
    else:
        print("Escribe tu edad correctamente")
if __name__ == '__main__':
    welcome = '🐱‍👤Bienvenido a la sala de juegos 🤖'
    print(welcome)
    run()