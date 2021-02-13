"""
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra,
y una de las funciones anteriores, y utilice la función pasada "del diccionario" para aplicar los descuentos
o el IVA a los productos de la cesta y devolver el precio final de la cesta
"""
def apply_discount(price, discount):
    return price - price * discount / 100
def apply_IVA(price, percentage):
    return price + price * percentage / 100
def price_basket(basket, calculo):
    total = 0
    for price, discount in basket.items():
        total += calculo(price, discount)
    return total
def run():
    print('El precio de la compra tras aplicar los descuentos es: ', price_basket({1000:20, 500:10, 100:1}, apply_discount))
    print('El precio de la compra tras aplicar el IVA es: ', price_basket({1000:20, 500:10, 100:1}, apply_IVA))
if __name__ == "__main__":
    run()