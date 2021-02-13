"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
def run():
    word = str(input("Escribe una palabra: "))
    for i in range (0, 11):
        print(word)
if __name__ == '__main__':
    run()