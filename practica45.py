"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos
y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando
de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""
def run():
    fruit = {
        "Platano": 1.35,
        "Manzana": 0.80,
        "Pera": 0.85,
        "Naranja" : 0.70
    }
    print("Bienvenido a la fruteria: ")
    print("Fruta - Precio")
    for key, value in fruit.items():
        print(key, end=" ")
        print(value)
    fruta = str(input("Escribe el nombre de la fruta que quieres comprar: "))
    fruta = fruta.capitalize()
    precio = 0
    multiplo = 0
    for i in fruit.keys():
        if i == fruta:
            fruta = i
            kg = float(input("Ingresa el numero de Kg, que quieres comprar de esa fruta: "))
            precio = fruit.get(i)
            multiplo = precio * kg
            print(f"La fruta que escogiste fue: {fruta} y el precio en kg es: {round(multiplo, 2)}")
        elif i != fruta:
            print(f"La fruta: {fruta}, No se encuentra disponible")
            break
if __name__ == "__main__":
    run()