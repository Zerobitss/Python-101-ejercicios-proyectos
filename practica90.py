"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen
a continuación.
* Ingredientes vegetarianos: Pimiento y tofu.
* Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con
los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas
la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

# Variables que incluyen el tipo de pizza y los ingredientes en listas
tipo_pizza =["Vegetariana", "No Vegetariana"]
ingred_vegetarianos = ["Pimiento", "Tofu"]
ingred_no_veggies = ["Peperoni", "Jamón", "Salmón"]

# Función que despliega el tipo de pizzas de la lista tipo_pizza
def imprime_tipo_pizzas(tipo_pizzas):
    contador = 1
    for pixa in tipo_pizza:
        print(f'\t{contador}.- {pixa}')
        contador += 1

# Función que regresa el tipo de pizza que el usuario quiere a partir de su elección numérica.
def elige_pizza(tipo_pizza, usuario_elige_pizza):
    if usuario_elige_pizza == 1:
        pizza = tipo_pizza[0]
        print(f'\n\tEl tipo de pizza seleccionada es {pizza}\n')
        
    else:
        pizza = tipo_pizza[1]
        print(f'\n\tEl tipo de pizza seleccionada es {pizza}\n')
    return pizza

# Funcion que pide muestra al usuario los ingredientes disponibles de acuerdo al tipo de pizza seleccionada y toma su elección para agregarla a la órden.
def selecciona_ingrediente(pizza):
    print(f'\t** Todas nuestras pizzas incluyen Mozarella y salsa Pomodoro')
    if pizza == "Vegetariana":
        print("\n\tElije un ingrediente para completar tu pedido: ")
        contador = 1
        for i in ingred_vegetarianos:
            print(f'\t{contador}.- {i}')
            contador += 1

        usuario_elige_ingrediente = int(input("\n\tElige un ingrediente (1/2): "))
        ingrediente = ingred_vegetarianos[usuario_elige_ingrediente - 1]
        print(f'\n\tEl ingrediente seleccionado es {ingrediente}\n')
    

    else:
        print("\n\tElije un ingrediente para completar tu pedido: ")
        contador = 1
        for i in ingred_no_veggies:
            print(f'\t{contador}.- {i}')
            contador += 1

        usuario_elige_ingrediente = int(input("\n\tElige un ingrediente (1/2/3): "))
        ingrediente = ingred_no_veggies[usuario_elige_ingrediente - 1]
        print(f'\n\tEl ingrediente seleccionado es {ingrediente}\n')
    return ingrediente

def orden(ingrediente, pizza):
    print(f'\tTu orden es la siguiente:\n\t   >> Pizza {pizza} con {ingrediente}')

if __name__ == "__main__":
    print("""
        >> Bienvenidx a La pizzería Bella Napoli <<
        Le ofrecemos las más deliciosas pizzas estilo Napolitano
        Puede elegir entre los siquientes tipos de pizza: 
        """)
    imprime_tipo_pizzas(tipo_pizza)
    usuario_elige_pizza = int(input("\n\t¿Qué tipo de pizza desea (1/2)?: "))
    pizza = elige_pizza(tipo_pizza, usuario_elige_pizza)
    ingrediente = selecciona_ingrediente(pizza)
    orden(ingrediente, pizza)
    print(f'\n\t>> Disfruta tu pizza y vuelve pronto <<')
    print(f'\n\t>> Sayonara <<')