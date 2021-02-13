class Persona():

    def __init__(self, apellidoPat, apellidoMat, nom):
        self.apellidoPaterno = apellidoPat
        self.apellidoMaterno = apellidoMat
        self.nombres = nom

    def mostrarNombre(self):
        txt = "{0}, {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

class Estudiante(Persona):

    def __init__(self, apellidoPat, apellidoMat, nom , pro):
#Se declaran los atributos a heredad
        super().__init__(apellidoPat, apellidoMat, nom)
#Se hace la declaracion de los atributos heredados
        self.profesion = pro

#El argumento "pro" se refiere a la profesion esto quiere decir que solamente va a poder ser utilizado en esta clase,
# ya que esta clase es para estudiante, del mismo modo pudiesemos crear otra clase para trabajador y colocar el puesto de trabajo

estudiante1 = Estudiante("Rojas", "Ollarves", "Jose", "Ingenieria de Sistemas")

print(estudiante1.mostrarNombre())
print(estudiante1.profesion)