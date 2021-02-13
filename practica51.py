"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario
donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario
si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número
de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará
del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad
pendiente de cobro.
"""
def run():
    factura = {}
    cobro = 0
    pagado = 0
    opcion = int(input("""
    Bienvenido que deseas hacer?

    1.- Añadir nueva factura
    2.- Pagar factura existente
    3.- Terminar

    Escribe tu opcion: """))
    while opcion == 1:
        print("Haz elegido la opcion: (Añadir nueva factura)")
        bill = str(input("Introduce el numero de la factura: "))
        cost = str(input("Introduce el valor de la factura: "))
        factura[bill] = cost
        continuar = str(input("Deseas agregar otra factura? (y/n): "))
        if continuar == "y":
            newbill = str(input("Ingresa el numero de la factura: "))
            newcost = str(input("Ingresa el costo de la factura: "))
            for i in zip(range(len(newbill)), range(len(newcost))):
                factura[newbill] = newcost
            for key, value in factura.items():
                print(f"El codigo de la factura: {key}", end=" ")
                print(f"Tiene un costo de {value}")
            opcion = int(input("Que deseas hacer ahora?: "))
        elif continuar == "n":
            for key, value in factura.items():
                print(f"El codigo de la factura: {key}", end=" ")
                print(f"Tiene un costo de {value}, fue agregada existosamente")
            opcion = int(input("Que deseas hacer ahora?: "))
    while opcion == 2:
        print("Haz elegido la opcion: (Pagar factura existente)")
        if any(factura) == True:
            for key in factura:
                factura[key] = int(factura[key])
            for i in factura.values():
                cobro = sum(factura.values())
            print(f"La cantidad pendiente por cobrar es: {cobro}")
            pay = str(input("Ingresa el numero de factura que deseas cobrar: "))
            for j in list(factura.keys()):
                if j == pay:
                    pagado = factura[pay]
                    result = cobro - pagado
                    del(factura[pay])
                    print(f"La factura numero: {pay} ha sido cobrada pagada exitosamente")
                    print(f"Fueron pagados: {pagado}")
                    print(f"Faltan por cobrar: {result}")
                    if any(factura):
                        continuar = str(input("Deseas cobrar otra factura?: (y/n) "))
                        if continuar == "y":
                            pay = str(input("Ingresa el numero de factura que deseas cobrar: "))
                        elif continuar == "n":
                            opcion = int(input("Que deseas hacer ahora?: "))
                elif j != pay:
                    print(f"El numero ingresado de la factura ({pay}) es incorrecto")
        else:
            print("No existen facturas pendientes por cobrar")
            opcion = int(input("Que deseas hacer ahora?: "))
    while opcion == 3:
        print("Haz elegido la opcion: (Terminar)")
        return False
if __name__ == "__main__":
    print("Bienvenido, aqui puedes gestionar las facturas pendientes \n")
    run()