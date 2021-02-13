"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces
que aparece la letra en la frase.
"""
def run():
    contador = 0
    word = str(input("Ingresa una frase: "))
    letter = str(input("Ingresa una letra: "))
    for i in word:
        if i == letter:
            contador +=1
    print(f"La cantidiad de veces que la letra {letter}, se repite en la palabra {word}, es: {contador}")
if __name__ == '__main__':
    run()