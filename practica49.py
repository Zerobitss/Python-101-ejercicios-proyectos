"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio
y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y
el coste total, con el siguiente formato

Lista de la compra
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""
def run():
    cesta = {}
    total = 0
    continuar = "y"
    while continuar == "y":
        producto = str(input("Ingresa el nombre del producto que quieres comprar: "))
        precio = int(input(f"Ingresa el precio de {producto}: "))
        cesta[producto] = precio
        continuar = str(input("Deseas seguir comprando? (y/n)"))
        if continuar == "y":
            print("Cesta actual de compra: \n")
            for key, value in cesta.items():
                print(f"Articulos de compra: {key}", end=" ")
                print(f"Precio de los articulos: {value}")
        else:
            print("Lista de la compra")
            for key, value in cesta.items():
                print(f"Articulos de compra: {key}", end=" ")
                print(f"Precio de los articulos: {value}")
            total = sum(cesta.values())
            print(f"Coste total: {total}")
    print("Gracias por su compra")
if __name__ == "__main__":
    print("Bienvenido al market")
    run()