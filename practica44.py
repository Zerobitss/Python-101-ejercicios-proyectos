"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar
por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
def run():
    diccionario = {}
    nombre = str(input("Ingresa tu nombre: "))
    edad = int(input("Ingresa tu edad: "))
    direccion = str(input("Ingresa tu Direccion: "))
    telefono =  str(input("Ingresa tu numero de telefono: "))
    diccionario["name"] = nombre
    diccionario["old"] = edad
    diccionario["address"] = direccion
    diccionario["phone"] = telefono
    print(diccionario["name"], "su edad: ", diccionario["old"], "vive en: ", diccionario["address"], "su telefono es: ", diccionario["phone"])
if __name__ == "__main__":
    run()