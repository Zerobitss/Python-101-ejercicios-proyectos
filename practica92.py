class Automovil:

    def __init__(self, modelo, marca, color, llantas, puertas, estado, motor):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = estado
        self._motor = motor
        self._llantas = llantas
        self._puertas = puertas

    def __str__(self):
        return f"Modelo: {self.modelo}\nMarca: {self.marca}\nColor: {self.color}\nEstado: {self._estado}\nMotor: {self._motor}\
        \nRuedas: {self._llantas}\nPuertas: {self._puertas}"

    @property
    def acelerar(self):
        return self._motor._combustible

    @acelerar.setter
    def set_acelerar(self, value):
        if value > 0:
            self._motor._combustible -= value
            print(self._motor._combustible)
        else:
            print(f"Tu combustible actual es: {self._motor._combustible}")

    def frenar(self):
        if self._estado == "Reposo":
            return "El carro esta parado"
        else:
            return "El carro esta en movimiento"

    def fill(self, can_combustible):
        self._motor._combustible = self._motor._combustible + can_combustible
        return self._motor._combustible

class Motor:
    def __init__(self, cilindros, tipo, combustible):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self._combustible = combustible

    def __str__(self):
        return f"Cilindros: {self.cilindros}\nTipo_Combustible: {self.tipo}\nCantidad_gasolina: {self._combustible}"


    def inyectar_combustible (self, cantidad):
        pass
def __init__()


def run():
    carro = Automovil("Spark", "Chevrolet", "Rojo", 4, 3, "Reposo", Motor(4, "Gasolina", 100))
    carro.fill(200)
    print(str(carro))
    carro.set_acelerar = 100
if __name__ == "__main__":
    run()
