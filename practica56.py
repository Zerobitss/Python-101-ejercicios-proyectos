"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función
area = pi * radio**2
cilindro = pi * radio ** 2 * altura
"""
def area_circulo():
    pi = 3.14
    radio = float(input("Ingresa el radio del circulo: "))
    area = pi * radio ** 2
    return area
def volumen_cilindro(area, altura):
    result = area * altura
    return result
if __name__ == "__main__":
    area = area_circulo()
    print(f"El area del circulo es: {area}")
    altura = float(input("Ingresa la altura del cilindro: "))
    print(volumen_cilindro(area, altura))