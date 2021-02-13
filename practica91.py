class Warrior:
    def __init__(self, faction, race, rol, genere, name, live):
        self.faction = faction
        self.race = race
        self.rol = rol
        self.genere = genere
        self.name = name
        self.live = live
    def __str__(self):
        return "Su faccion es: {}\nSu raza es: {}\nSu rol es:{}\nSu genero es: {}\nSu nombre es:{}"\
            .format(self.faction, self.race, self.rol, self.genere, self.name)
    def accion(self):
        if self.rol == "DPS":
            return "Te ataco con mi AXE"
        elif self.rol == "TANK":
            return "Yo soy el tanque del equipo"
        elif self.rol == "HEALER":
            return "Yo curare al equipo"
        else:
            return "No tengo ningun rol asignado"

def run():
    personaje = Warrior("Horda", "Orco", "DPS", "Hombre", "Thrall", 10)
    print(str(personaje))
    print(personaje.accion())

if __name__ == "__main__":
    run()