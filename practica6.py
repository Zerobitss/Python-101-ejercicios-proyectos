"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e
imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas.
"""
def run():
    login = str(input("Ingresa tu correo: "))
    passw = str("sixsamurai123*")
    password = str(input("Escribe tu contraseña: "))
    password = password.lower()
    if passw == password:
        print(f"Usuario introducido coincide perfectamente: {login}")
        print(f"La contraseña introducida coincide perfectamente: {passw}")
    else:
        print("Contraseña incorrecta")
if __name__ == '__main__':
    run()