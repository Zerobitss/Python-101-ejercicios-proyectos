"""
Realizar una funcion que mediante al valor que reciba haga algun tipo de calculo  + - * /
"""
def menu(opcion):
    print("1.- Suma \n2.- Resta \n3.- Multiplicacion \n4.- Division ")
    if opcion == 1 and opcion > 0:
        n1 = int(input("Ingresa el primer numero: "))
        n2 = int(input("Ingresa el segundo numero: "))
        return n1 +n2
    elif opcion == 2:
        n1 = int(input("Ingresa el primer numero: "))
        n2 = int(input("Ingresa el segundo numero: "))
        return print(n1 - n2)
    elif opcion == 3:
        n1 = int(input("Ingresa el primer numero: "))
        n2 = int(input("Ingresa el segundo numero: "))
        return print(n1 * n2)
    elif opcion == 4:
        n1 = int(input("Ingresa el primer numero: "))
        n2 = int(input("Ingresa el segundo numero: "))
        return print(n1 / n2)
    else:
        print("Opcion invalida porfavor escribe una opcion correcta dentro del menu")
def run():
    opcion = int(input("Ingresa la opcion: "))
    print(menu(opcion))
if __name__ == "__main__":
    run()