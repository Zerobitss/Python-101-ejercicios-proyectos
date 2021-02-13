"""
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3,
y muestre por pantalla la lista resultante.
"""
def run():
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(len(abecedario), 1, - 1):
        if i % 3 == 0:
            abecedario.pop(i - 1)
        else:
            continue
    print(f"El nuevo abecedario es: {abecedario}")
if __name__ == '__main__':
    run()