"""
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación
comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios.

Los puntos que pueden conseguir que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre
las cifras mencionadas.

A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida
en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	            Puntuación
1. Inaceptable	      0.0
2. Aceptable	      0.4
3. Meritorio	      0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá
el usuario.
"""
def run():
    puntuacion = int(input("Eligue cual es tu puntuacion:"))
    salario = 2_400
    while True:
        if puntuacion == 1:
            print(f"Tu nivel es Inaceptable y tu sueldo es {salario}")
            break
        elif puntuacion == 2:
            print(f"Tu nivel es Aceptable y tu sueldo es {salario*2}")
            break
        elif puntuacion == 3:
            print(f"Tu nivel es Meritorio y tu sueldo es: {salario*3}")
            break
        else:
            print("Escoge una opcion correcta")
            return False
if __name__ == '__main__':
    menu = """
    Nivel	            Puntuación
    1. Inaceptable	      0.0
    2. Aceptable	      0.4
    3. Meritorio	      0.6 o más
    """
    print(menu)
    run()