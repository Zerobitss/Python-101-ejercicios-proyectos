"""
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
"""
def saludo(nombre):
    print(f"Saludos {nombre}!")
def suma(n1, n2):
    return n1+n2
if __name__ == "__main__":
    nombre = str(input("Escribe tu nombre: "))
    saludo(nombre)
    n1 = int(input("escribe un numero: "))
    n2 = int(input("escribe un numero: "))
    result = suma(n1, n2)
    print(result)