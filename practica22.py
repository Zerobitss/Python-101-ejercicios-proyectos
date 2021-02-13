"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y
muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""
def run():
    cantidad_inv = int(input("Ingresa la cantidad a invertir: "))
    interes = int(input("Ingrese el interes anual: "))
    year = int(input("Numero de años: "))
    for i in range(year):
        capital = calculo_interes(cantidad_inv, interes, i+1)
        print(f"Capital obtenido en el {i} año, es: {round(capital,2)}")
def calculo_interes(cantidad_inv, interes, year):
    result = (cantidad_inv * (1 + interes / 100) ** year)
    return result
if __name__ == '__main__':
    run()