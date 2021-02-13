"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses,
que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience
leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular
y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
def porcentaje(num1, num2):
    porcentaje = num1 * num2 / 100
    return porcentaje
def run():
    deposito = float(input("Ingresa la cantidad a depositar en tu cuenta de ahorros: "))
    porcent = float(4)
    result = porcentaje(deposito, porcent)
    print(f"La cantidad de ahorros tras el primer año agregada a tu cuenta sera de: {round(result, 2)}$")
    print(f"La cantidad de ahorros tras el segundo año agregada a tu cuenta sera de: {round(result, 2)*2}$")
    print(f"La cantidad de ahorros tras el tercer año agregada a tu cuenta sera de: {round(result, 2)*3}$")
if __name__ == '__main__':
    run()