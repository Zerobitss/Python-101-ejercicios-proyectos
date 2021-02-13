"""
(2) Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas
de la lista.
"""
def run():
    cursos = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    for i in cursos:
        print(f"Yo estudio: {i}")
    print(f"Un total de: {len(cursos)} Cursos")
if __name__ == "__main__":
    run()