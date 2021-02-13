"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior
a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre
por pantalla el grupo que le corresponde.
"""
def run():
    name = str(input("Ingresa tu nombre: "))
    name = name.lower()
    sexo = str(input("Ingresa tu sexo: "))
    sexo = sexo.lower()
    if (name < 'm') and (sexo == 'mujer'):
        print("grupo a")
    if (name > 'n') and (sexo == 'hombre'):
        print("grupo b")
if __name__ == '__main__':
    run()