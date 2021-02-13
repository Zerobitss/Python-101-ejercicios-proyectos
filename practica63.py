"""
1: Pidele al usuario que ingrese dos numeros enteros por teclado
y determine los siguientes aspectos.

1: Si ambos numeros son iguales
2: Si los numeros son diferentes
3: Si el primero  es mayor al segundo
4: Si el segundo es mayor al primero
"""
def run():
    num_1 = int(input("Ingresa el primer numero: "))
    num_2 = int(input("Ingresa el segundo numero: "))
    if num_1 and num_2:
        print("Son iguales")
    elif num_1 != num_2:
        print("Son diferentes")
    elif num_1 > num_2:
        print("El primer numero es mayor que el segundo")
    elif num_1 < num_2:
        print("El segundo numero es mayor que el primero")
if __name__ == "__main__":
    run()