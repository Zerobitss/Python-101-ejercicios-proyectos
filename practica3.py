"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa
que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de
una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""
def run():
    venta = int(input("Ingrese el numero de barras de pan vendidas que no son del dia: "))
    pan_fresco = 3.49
    descuento = 60
    pan_frescof = 3.49 * venta
    oferta = pan_frescof * descuento / 100
    precio_final = pan_frescof - oferta
    print(f"El precio habitual de un pan fresco es: {pan_fresco}€")
    print(f"Los panes que no son del dia tienen un descuento del 60%")
    print(f"tu descuento total seria de: {round(oferta, 2)}€, y su coste final seria {round(precio_final, 2)}€")
if __name__ == '__main__':
    run()