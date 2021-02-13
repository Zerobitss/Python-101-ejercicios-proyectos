"""
1) Identifica el tipo de dato (int, float, string o list) de los siguientes
valores literales.

"Hola Mundo"
[10, 1, 200]
-30
1.0
["Pedro", "Jorge]
"""
def run():
    print("Hola mundo - Esto es un string")
    lista = [10, 1, 200]
    print(f"Esto es una lista: {lista}")
    entero = -30
    print(f"Esto es un entero negativo: {entero}")
    decimal = 1.0
    print(f"Esto es un numero flotante o decimal: {decimal}")
    lista_1 = ["Pedro", "Jorge"]
    print(f"Esta es otra lista: {lista_1}")
if __name__ == "__main__":
    run()