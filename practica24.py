"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
def run ():
    for i in range (1, 11):
        for j in range(1, 11):
            print(i*j, end= "\t")
        print("")
if __name__ == '__main__':
    run()