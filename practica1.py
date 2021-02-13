"""
Una juguetería tiene mucho éxito en dos de sus productos: payaso y muñeca. Suele hacer venta por correo y la empresa
de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
cada paquete a demanda. Cada payaso pesa 112 g y la muñeca 75 g. Escribir un programa que lea el número de payasos y
muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
def run():
    peso_payaso = 112
    peso_muneca = 75
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
    3.- Terminar compra
    4.- Salir

    Eligue tu opcion: """))
        if menu == 1:
            payaso_cant = int(input("Escribe la cantidad de payasos que quieres comprar: "))
            peso_payaso *= payaso_cant
        elif menu == 2:
            muneca_cant = int(input("Escribe la cantidad de muñeca que quieres comprar: "))
            peso_muneca *= muneca_cant
        elif menu == 3:
            pedido = peso_payaso + peso_muneca
            print(f"Gracias por su compra, el peso total de su pedido es: {pedido}g")
            print("Espero volverte a ver pronto por aqui, hasta luego 😁")
            return False
        elif menu == 4:
            print("Espero volverte a ver pronto por aqui, hasta luego 😁")
            return False
if __name__ == '__main__':
    run()