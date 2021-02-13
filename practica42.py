"""
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla
el menor y el mayor de los precios.
"""
def run():
    precios = [50, 75, 46, 22, 80, 65, 8]
    precios.sort()
    minimo = min(precios)
    maximo = max(precios)
    print(f"El menor de los precios es: {minimo}")
    print(f"El mayor de los precios es: {maximo}")
if __name__ == '__main__':
    run()