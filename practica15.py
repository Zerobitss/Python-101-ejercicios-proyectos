"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e
imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas.
"""
def run():
    password = "sixsamurai123*"
    in_pass = str(input("Ingresa tu contraseña: "))
    if in_pass.lower() == password:
        print(f"Felicidades si coincide tu contraseña: {password}")
    else:
        print("Contraseña no coinciden")
if __name__=='__main__':
    run()