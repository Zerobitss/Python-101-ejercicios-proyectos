"""
3) El siguiente codigo pretende realizar una media entre 3 numeros
pero algo anda mal, ¿Podes identificar el problema y solucionarlo?

num_1 = 9
num_2 = 3
num-3 = 6
media = num_1 + num_2 + num_3 / 3
print("La nota media es", media)
"""
def run():
    num_1 = 9
    num_2 = 3
    num_3 = 6
    media = (num_1 + num_2 + num_3) / 3 #El problema es que no se da prioridad a la suma de la ecuacion por que no tenia ()
    print("La nota media es", media)
if __name__ == "__main__":
    run()