"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal
"""
def run():
    word = str(input("Introduce una palabra: "))
    vocals = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocals:
        times = 0
        for letter in word:
            if letter == vocal:
                times += 1
        print(f"La vocal {vocal}, aparece : {times} veces")
if __name__ == '__main__':
    run()
