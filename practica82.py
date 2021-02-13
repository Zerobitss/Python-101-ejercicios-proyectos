"""
(4) Crea una funcion que nos devuelva numeros pares.
"""
def num_par (numero):
    if numero % 2 == 0:
        print(f"El numero: {numero}, es par")
    else:
        print(f"El numero: {numero}, es impar")
def run():
    numero = int(input("Ingresa un numero entero: "))
    num_par(numero)
if __name__ == "__main__":
    run()