"""
(1) Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
"""
def funcion():
    nombre = str(input("Ingresa tu nombre: "))
    return nombre
def run():
    resultado = funcion
    print(f"Saludos: {resultado}")
if __name__ == "__main__":
    run()