"""
(1) Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla.
"""
def run():
    cursos = []
    while len(cursos) < 6:
        asignatura = str(input("Ingresa la asignatura de tus cursos: "))
        cursos.append(asignatura)
        if len(cursos) >= 5:
            print(f"Haz llegado al limite de asignaturas, para tu semestre")
            break
    for i in cursos:
        print(f"Las asignatura: {i}, Se ha agregado exitosamente")
if __name__ == "__main__":
    run()