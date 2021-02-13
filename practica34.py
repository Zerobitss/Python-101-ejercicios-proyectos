"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
"""
def run():
    asignaturas = ["Matematicas", "Fisica", "Quimica ", "Historia", "Lengua"]
    for i in range(len(asignaturas)):
        print(f"Yo estudio: {asignaturas[i]}")
if __name__ == '__main__':
    run()