"""
(4)Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""
def run():
    while True:
        word = str(input("Ingresa una palabra: "))
        word = word.lower()
        if word == "salir":
            print("Haz salido del sistema")
            return False
        else:
            print("Sigue escribiendo, si quieres salir debes escribir (salir)")
if __name__ == "__main__":
    run()