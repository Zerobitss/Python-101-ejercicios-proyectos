"""
2) Determina sin programar el resultado que aparecera en la pantalla
a partir de las siguientes variables:
a = 20
b = 10
c = "Pepe"
d = [1,2,3]

print(a*4)
print(a-b)
print(c+ "Mundo")
prin(* 2)
print(c[-1])
print(c[1:])
print(d+d)

"""
def run():
    a = 20
    b = 10
    c = "Pepe"
    d = [1,2,3]

    print(a*4) #80
    print(a-b) #10
    print(c+ "Mundo") #PepeMundo"
    print(c * 2) #PepePepe
    print(c[-1]) #Imprimir la posicion del caracter, en este caso la ultima que sera e
    print(c[1:]) #Imprimir la cadena de texto empezando desde su segundo valor.
    print(d+d) # [1, 2, 3, 1, 2, 3]
if __name__ == "__main__":
    run()