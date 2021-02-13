"""
(1)Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña
hasta que introduzca la contraseña correcta.
"""
def run():
    while True:
        password = str(input("Ingresa tu contraseña: "))
        re_password = str(input("Repite tu contraseña: "))
        if password == re_password:
            print(f"Tu contraseña coinciden: {re_password}")
            print("Bienvenido!")
            return False
        else:
            print(f"Tu contraseñas no son iguales, tu primera contraseña fue: ({password})\t Tu segunda contraseña fue: ({re_password}), porfavor intenta de nuevo")
if __name__ == "__main__":
    run()