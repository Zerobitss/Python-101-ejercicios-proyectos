"""
3: Con operadores logicos, determina si una cadena de texto ingresada por el usuario
tiene una longitud mayor o igual a 3 y a su vez es menor a 10. (true o false)
"""
def run():
    texto = str(input("Ingresa un texto: "))
    if len(texto) >= 3 and len(texto) < 10:
        print(True)
    else:
        print(False)
if __name__ == "__main__":
    run()