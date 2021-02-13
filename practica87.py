"""
Una juguetería tiene mucho éxito en dos de sus productos: payaso y muñeca. Suele hacer venta por correo y la empresa
de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
cada paquete a demanda. Cada payaso pesa 112 g y la muñeca 75 g. Escribir un programa que lea el número de payasos y
muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
def run():
    payaso_cant = 0
    muneca_cant = 0
    precio_payaso = 100
    precio_muneca = 90
    payaso_peso = 112
    muneca_peso = 75
    pedido = 0
    menu_inicio =("""
        🤖Bienvenido a la jugeteria👾
    Los jugetes disponibles en este momento son:
    1.- Payasos, costo = 100$, su peso es de 112g
    2.- Muñeca, costo = 90$, su peso es de 75g
    """)
    print(menu_inicio)
    while True:
        menu = int(input("""
    Que jugetes deseas comprar?

    1.- Payaso
    2.- Muñeca
    3.- Salir

    Eligue tu opcion: """))
        if menu == 1:
            payaso_cant = int(input("Ingrese la cantidad de payasos que quiere comprar: "))
            precio_payaso *= payaso_cant
            payaso_peso *= payaso_cant
            print(f"Su pedido es un total de: {precio_payaso}$ Pesos y el peso de su paquete es: {payaso_peso}g")
            menu = int(input("""Quieres seguir comprando?:
            1.- Si
            2.- Terminar compra
            Escribe tu opcion: """))
            if menu == 1:
                print(f"Su pedido actual es: {precio_payaso}$ Pesos y el peso de su paquete es: {payaso_peso}g")
            elif menu == 2:
                precio_final = precio_payaso
                peso_final = payaso_peso
                print(f"Su pedido final es de: {precio_final}$, y el peso de su paquete es: {peso_final}")
                print("Espero volverte a ver pronto por aqui, hasta luego 😁")
                return False
            else:
                print("Escribe una opcion correcta")
        elif menu == 2:
            muneca_cant = int(input("Ingrese la cantidad de muñecas que desea comprar: "))
            precio_muneca *= muneca_cant
            muneca_peso *= muneca_cant
            print(f"Su pedido es un total de: {precio_muneca}$ Pesos y el peso de su paquete es: {muneca_peso}g")
            menu = int(input("""Quieres seguir comprando?:
            1.- Si
            2.- Terminar compra
            Escribe tu opcion: """))
            if menu == 1:
                print(f"Su su pedido actual es: {precio_muneca}$ Pesos y el peso de su paquete es: {muneca_peso}g ")
            elif menu == 2:
                precio_final = precio_payaso + precio_muneca
                peso_final = payaso_peso + muneca_peso
                print(f"Su pedido final es de: {precio_final}$, y el peso de su paquete es: {peso_final}")
                print("Espero volverte a ver pronto por aqui, hasta luego 😁")
                return False
            else:
                print("Escribe una opcion correcta")
        elif menu == 3:
            print("Espero volverte a ver pronto por aqui, hasta luego 😁")
            return False
        else:
            print("Escribe una opcion valida")
if __name__ == '__main__':
    run()