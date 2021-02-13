"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
debe imprimirse el contenido del diccionario.
"""
def run():
    d = {}
    continuar = "y"
    while continuar == "y":
        key = input("Que dato quieres ingresar: ")
        value = input(key + ": ")
        d[key] = value
        print(d)
        continuar = input("Deseas seguir agregando contenido? (y/n): ")
        if continuar != "y":
            print(f"Estos son todos los datos que haz ingresado {d}")
    print("haz salido del programa")
if __name__ == "__main__":
    run()
