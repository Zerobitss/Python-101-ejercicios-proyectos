"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
def run():
    asignaturas = ["Matematicas", "Fisica", "Quimica ", "Historia", "Lengua"]
    notas = []
    print(f"Asignaturas: {asignaturas}")
    for i in range(len(asignaturas)):
        i = int(input(f"Ingresa la nota que haz sacado en {asignaturas[i]}: "))
        notas.append(i)
    for j in range(len(notas)):
        if (notas[j] > 5):
            print(f"Aprobaste: {asignaturas.pop()}")
    print(f"Las asignaturas que debes repetir son: {asignaturas}")
if __name__ == '__main__':
    run()