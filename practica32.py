"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""
def run():
    while True:
        eco = str(input("Introduce una palabra: "))
        eco.lower()
        if eco == "salir":
            print("Haz salido")
            return False
        else:
            print(eco)
if __name__ == '__main__':
    run()