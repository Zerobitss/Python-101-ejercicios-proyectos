class Catalogo():
    def __init__(self, juegos = []):
        self.juegos = juegos

    def __str__(self):
        return f"{self.juegos}"

    def agregar(self, juego):
        self.juegos.append(juego)
        print(f"Se ha agregado exitosamente {juego}\n")

    def mostrar(self):
        for i, k in enumerate(self.juegos, 1):
            print(f"{i}: {k}")

    def seleccion(self, ide): #Hacer un metodo get para obtener directamente el argumento con el array o lista
        for i in self.juegos:
            if ide == i:
                print(f"Haz seleccionado: {ide}")

    def __len__(self):
        return self.juegos

class Game():
    def __init__(self, codigo, nombre, categoria, numJugador, plataforma):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.numJugador = numJugador
        self.plataforma = plataforma
        print(f"Haz comprado {self.nombre}")

    def __str__(self):
        return f"Codigo: {self.codigo}\nTitulo:{self.nombre}\nCategoria: {self.categoria}\nNumero de jugadores: {self.numJugador}\nPlataforma: {self.plataforma}"

class nintendoSwitch():
    def __init__(self, color, modelo, product):
        self.color = color
        self.modelo = modelo
        self.product = product

    def __str__(self):
        return f"Informacion acerca de la consola: \nModelo: {self.modelo}\nColor: {self.color}\nEstado: {self.product}"

    def play(self, jugar):
        print(f"Haz iniciado el juego: {jugar}")

    def estado(self, valor = False):
        if valor == True:
            print("Consola encendida lista para jugar!")
        elif valor == False:
            print("Consola apagada")
        else:
            print("Comando no disponible porfavor intente (True/False)")


def run():
    juego1 = Game('001', 'Zelda Breath of the wild', 'Rol', 1, 'Nintendo Switch')
    juego2 = Game('002', 'Pokemon Sword', 'Aventura', 1, 'Nintendo Switch')
    juego3 = Game('003', 'Super Mario Odessy', 'Aventura', 2, 'Nintendo Switch')
    juego4 = Game('004', 'Crash Bandicoot Trilogy', 'Aventura', 1, 'Nintendo Switch')
    bibloteca = Catalogo([juego1, juego2, juego3, juego4])
    bibloteca.agregar(Game("005","DOOM Eternal", "FPS", 1, 'Nintendo Switch'))
    bibloteca.mostrar()
    nintendo = nintendoSwitch("Gris", "2019", "Nuevo")
    print(nintendo)
    nintendo.estado(True)
    print("***************")
    #bibloteca.seleccion('001')
    #print(len(bibloteca))
    nintendo.play(Game('006', 'Zelda Breath of the wild', 'Rol', 1, 'Nintendo Switch'))
    #nintendo.play(bibloteca.seleccion('001'))



if __name__ == "__main__":
    run()

