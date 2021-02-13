"""
(2) Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no,
valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".

"""
def validacion():
    email = str(input("Ingresa tu correo electronico: "))
    if "@" in email:
        print(f"Tu correo {email}, es valido")
    else:
        print(f"Tu correo {email}, es invalido")
def run():
    validacion()
if __name__ == "__main__":
    run()