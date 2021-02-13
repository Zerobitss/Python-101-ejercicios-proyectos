"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa
y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""
def run():
    diccionario = {
        'Euro':'€',
        'Dollar':'$',
        'Yen':'¥'
    }
    divisa = str(input("Ingresa el nombre de una divisa: "))
    divisa = divisa.capitalize()
    if divisa == "Euro":
        print(diccionario.get("Euro"))
    elif divisa == "Dollar":
        print(diccionario.get("Dollar"))
    elif divisa == "Yen":
        print(diccionario.get("Yen"))
    else:
        print("Divisa no disponible")
if __name__ == '__main__':
    run()