"""
Crear un mazo de cartas añadiendo las cartas a una lista usando bucles
"""
def run():
    tantos = ["A", "2", "3", "4", "5", "6", "7", "S", "C", "R"]
    palos = ["oros", "copas", "espadas", "bastos"]
    baraja = []
    for tanto in tantos:
        for palo in palos:
            baraja.append(f"Simbolo: {tanto}, valor: {palo}")
            print(f'{tanto} de {palo}')
    print(baraja)
if __name__ == '__main__':
    run()