"""
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que
reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice
la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.
"""
def apply_IVA(price, percentage):
    '''
    Función que aplica un IVA a una cantidad.
    Parámetros:
        price: Es un valor real con el precio al que aplicar el IVA.
        percentage: Es el porcentaje del IVA a aplicar.
    Devuelve:
        El precio final tras aplicar el IVA.
    '''
    return price + price * percentage / 100

def apply_discount(price, percentage):

    return price + price * percentage / 100

def price_basket(basket, function):
    '''
    Función que calcula el precio de una cesta de la compra una vez aplicada una función a los precios iniciales.
    Parámetros:
        basket: Es un diccionario formado por pares precio:descuento.
        function: Es una función que toma dos valores reales y devuelve otro. Normalmente para aplicar descuentos o IVA.
    Devuelve:
        El precio final de la cesta de la compra una vez aplicada la función sobre los precios iniciales.
    '''
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total

print('El precio de la compra tras aplicar los descuentos es: ', price_basket({1000:20, 500:10, 100:1}, apply_discount))
print('El precio de la compra tras aplicar el IVA es: ', price_basket({1000:20, 500:10, 100:1}, apply_IVA))
