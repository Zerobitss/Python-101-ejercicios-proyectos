"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo,
de altura el número introducido.
*
**
***
****
*****
"""
def run():
    num = int(input("Ingresa un numero entero: "))
    triangulo = "*"
    print(f"La altura del triangulo rectangulo es: {num}")
    for i in range(num+1):
        print(triangulo * i)
if __name__ == '__main__':
    run()