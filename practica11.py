"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
    Renta	Tipo impositivo
    Menos de 10000€	5%
    Entre 10000€ y 20000€	15%
    Entre 200000€ y 35000€	20%
    Entre 350000€ y 60000€	30%
    Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
def run():
    ingreso_anual= int(input("Ingrese su ingreso anual: "))
    if ingreso_anual < 10_000 :
        print("Su tipo impositivo que le corresponde es de 5%")
    elif (ingreso_anual > 10_000) and (ingreso_anual < 20_000):
        print("Su tipo de impositivo que le corresponde es de 15%")
    elif (ingreso_anual > 200_000) and (ingreso_anual > 350_000):
        print("Su tipo de impositivo que le corresponde es de 30%")
    elif (ingreso_anual > 650_000):
        print("Su tipo de impositivo que le corresponde es de 45%")
if __name__ == '__main__':
    table = """
    Renta	               Tipo impositivo
    Menos de 10000€	            5%
    Entre 10000€ y 20000€	    15%
    Entre 200000€ y 35000€	    20%
    Entre 350000€ y 60000€	    30%
    Más de 600000€	            45%
    """
    print(table)
    run()