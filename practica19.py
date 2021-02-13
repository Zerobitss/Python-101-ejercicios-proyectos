"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
def run():
    age = int(input("Escribe tu edad: "))
    for i in range(age):
        i += 1
        if i == 1:
            print(f"Haz cumplido: {i} año")
        print(f"Haz cumplido: {i} años")
    print(f"Para un total de: {age} años")
if __name__ == '__main__':
    run()