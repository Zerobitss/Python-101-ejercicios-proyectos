"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en
el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso,
y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""
def run():
    cursos = {
        "Matematica": 6,
        "Fisica": 4,
        "Quimica": 5
    }
    for i, j in cursos.items():
        print(f"Asignaturas: {i}", end="/ Tiene ")
        print(f"Creditos: {j}")
    total = sum(cursos.values())
    print(f"El total de credito del curso son: {total}")
if __name__ == "__main__":
    run()