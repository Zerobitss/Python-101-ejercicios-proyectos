"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje
En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
notas introducidas por el usuario.
"""
def run():
    asignaturas = ["Matematicas", "Fisica", "Quimica ", "Historia", "Lengua"]
    notas = []
    print(asignaturas)
    for i in range(len(asignaturas)):
        i = int(input(f"Ingresa la nota que haz sacado en {asignaturas[i]}: "))
        notas.append(i)
    for j in range(len(asignaturas)):
        print(f"Asignatura: {asignaturas[j]}, haz sacado nota: {notas[j]}")
if __name__ == '__main__':
    run()