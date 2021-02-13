"""
4) Aqui hay otro problema, ¿Eres capaz de resolverlo? Al querer sumar entrada mas 10
nos sale un error.¿Que es lo que esta faltando?

entrada = input("Introduzca un numero: ")
Introduzca un numero: 20
entrada + 10
"""
def run():
    entrada = int(input("Introduzca un numero: "))
    entrada = entrada + 10 #El input retorna un valor de string, asi que hace falta transformar este valor a numerico
    print(f"El resultado es: {entrada}")
if __name__ == "__main__":
    run()