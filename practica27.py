"""
Realizar un ciclo for anidado para x, y
"""
def run():
    for x in range(1, 4):
        for y in range(1, 4):
            print(x, y) #Por cada valor de x, y va a ir sumandose, por esto y, cuando 1 vale 1 y pasa a ser 1 2 3, etc
        print() # Salto de linea
if __name__ == '__main__':
    run()