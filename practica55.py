"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA
y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA,
deberá aplicar un 21%.
"""
def factura(cantidad, iva):
    calculo = pago * iva
    return round(calculo, 2)
if __name__ == "__main__":
    pago = float(input("Ingresa la cantidad a pagar: "))
    iva = 0.21
    result = factura(pago, iva)
    print(f"El total de la factura es: {result}")