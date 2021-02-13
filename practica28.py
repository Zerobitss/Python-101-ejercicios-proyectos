"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña
hasta que introduzca la contraseña correcta.
"""
def run():
    password = str(input("Ingresa contraseña: "))
    re_password = str(input("Repite la contraseña: "))
    while password != re_password:
        print("Error contraseñas no coincen")
        password = str(input("Ingresa nuevamente la contraseña: "))
        re_password = str(input("Repite la contraseña: "))
    if password == re_password:
        print(f"Felicidades ambas contraseñas coinciden: {password}")
        break
if __name__ == '__main__':
    run()