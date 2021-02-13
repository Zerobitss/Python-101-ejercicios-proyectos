import sys
def run():
    if len(sys.argv) == 3:
        texto = sys.argv[1]
        repeticion = int(sys.argv[2])
        for i in range(repeticion):
            print(texto)
    else:
        print("Debes colocar al menos dos argumentos en el script")
if __name__ == "__main__":
    run()