# opcion = int(input("Eligue una opcion (1, 2 , 3): "))

# def conversacion(mensaje):
#     print("hola")
#     print("Como estas")
#     print(f"Elegiste la opcion: {mensaje}")
#     print("adios")

# conversacion(opcion)

# def decorador(func): #A, #B

#     def nueva_funcion():
#             print("Ejecutando la funcion")
#             #Aqui es donde se agrega la logica que va a ser añadida a la funcion
#             func()
#             print("Se ejecuto la funcion")

#     return nueva_funcion #C

# @decorador #Aqui es donde se le agrega la decoracion, la funcion que queramos
# def saluda(): #C
#     print("Hola mundo")

# saluda()


def decorador(func):
    def before_action():
        print("Vamos a ejecutar la funcion")
    def after_action():
        print("Se ejecuto la funcion")

    def nueva_funcion(*args, **kwargs):
        before_action()
        resultado = func(*args, **kwargs) #La ejecuto
        after_action()
        return resultado

    return nueva_funcion

@decorador
def saluda():
    print("hola, mundo")

@decorador
def suma(num1, num2):
    return num1 + num2

resultado = suma(10, 5)
print(resultado)
saluda()