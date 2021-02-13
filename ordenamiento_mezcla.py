import random

def ordenamiento_mezcla(lista):
    if len(lista) > 1:#Validar si existen valores en la lista
        medio = len(lista) //2#Encontrar el medio
        izquierda = lista[:medio]#Lista izquierda
        derecha = lista[medio:]#Lista derecha

        #Llamada recursiva en cada mitad
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha) #Ambas se ejecutaran hasta que se logre encontrar la lista deseada

        #Iteradores para recorrer la sublista
        i = 0
        j = 0

        #Iterador para la lista principal
        k =0

        while i < len(izquierda) and j < len(derecha): #Es decir mientras podamos seguir creando comparaciones
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:#Si la derecha es mas grande que la izquierda
                lista[k] = derecha[j]
                j += 1

            k += 1 #Esto es para evitar que el bucle no se dirija al infinito

        while i < len(izquierda):#Esto se aplica para lo que reste de la sublista, mientras podamos comparar
            lista[k] = izquierda[i]
            i+= 1
            k+= 1

        while j < len(derecha):#Estos se aplican ya para lo que reste de las sublista, mientras podamos comparar
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista
def run():
    tamano_lista = int(input("De que tamaño sera tu lista: "))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]

    print(lista)
    print('-'*10)

    lista_ordenada = ordenamiento_mezcla(lista)
    print(lista_ordenada)


if __name__ == "__main__":
    run()