"""
(2) Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
def run():
    word = str(input("Ingresa una palabra: "))
    for i in range(1, 11):
        print(f"{i}:", word)
if __name__ == "__main__":
    run()