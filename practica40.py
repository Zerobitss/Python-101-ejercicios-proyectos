"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""
def run():
    word = str(input("Ingresa una palabra: "))
    word= word.lower()
    reversa = word[::-1]
    if word == reversa:
        print(f"La palabra {word}, es palindromo")
    else:
        print(f"La palabra {word}, no es palindromo")
if __name__ == '__main__':
    run()