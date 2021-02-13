"""
(5)Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
def run():
    user = int(input("Ingresa tu edad: "))
    ingresos = int(input("Ingresa la cantidad de tus ingresos mensuales en €: "))
    if user > 16 and ingresos >= 1000:
        print("Puedes tributar")
    else:
        print("No puedes tributar")
if __name__ == "__main__":
    run()