"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
def run():
    edad = int(input("Ingresa tu edad: "))
    ingresos = int(input("Ingresa tus ingresos mensuales: "))
    if (edad >= 16) and (ingresos >= 1000):
        print("El usuario tiene que tributar")
        print(f"Puesto que tiene suficiente: {edad} y sus ingresos son mayores a: {ingresos}€")
    else:
        print("El usuario aun no puede tributar")
if __name__ == '__main__':
    run()
