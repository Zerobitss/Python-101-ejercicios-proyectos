"""
(3) Crea una funcion con argumentos interminables, luego itera con un bucle sobre los argumentos y agregale clave y valor
"""
def interminable(**kwargs):
    print(f"Datos ingresados: {kwargs}")
    return kwargs
def run():
    cliente = interminable(nombre = input("nombre: "), edad = input("edad: "), correo = input("correo: "), telefono = input("telefono: "))
    for i in cliente:
        print(f"Sus datos: {i}, sus valores: {cliente[i]}")
if __name__ == "__main__":
    run()