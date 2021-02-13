"""
(4) Mete los valores del 1 al 100 en una lista.
"""
def run():
    lista = []
    a = 101
    if len(lista) < a:
        for i in range(len(lista), a):
            lista.append(i)
        if len(lista) == a:
            for j in range(1, len(lista)):
                print(f"Los valores: {lista[j]} se han agregado a la lista")
if __name__ == "__main__":
    run()