class Mago():
    def __init__(self):
        pass
    def accion(self):
        print("Bola de fuego")

class Warrior():
    def __init__(self):
        pass
    def accion(self):
        print("Ataque de furia")

class Arquero():
    def __init__(self):
        pass
    def accion(self):
        print("Ataque con arco")

def accion_personaje(objeto):
    objeto.accion()

def run():
    personaje = Warrior()
    accion_personaje(personaje)

if __name__ == "__main__":
    run()