"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla.
"""
def run():
    cursos = ["Matematicas", "Fisica", "Quimica ", "Historia", "Lengua"]
    print("Asignaturas: ")
    for i in cursos:
        print(i)
if __name__ == '__main__':
    run()