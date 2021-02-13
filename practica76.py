"""
(3) Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
def run():
    nombre = str(input("Ingresa tu nombre: "))
    edad = int(input("Ingresa tu edad: "))
    direccion = str(input("Ingresa tu direccion: "))
    telefono = str(input("Ingresa tu numero de telefono: "))
    user = {
        'name': nombre,
        'age': edad,
        'address': direccion,
        'phone': telefono
    }
    for i, j in user.items():
        print(f"Su {i} es: {j}")
if __name__ == "__main__":
    run()