"""
(3) Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
def run():
    edad = int(input("Ingresa tu edad: "))
    for i in range(1, edad + 1):
        print(f"Haz cumplido: {i}")
if __name__ == "__main__":
    run()