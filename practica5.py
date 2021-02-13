"""
Escribre un programa que le pregunte al usuario la fecha de nacimiento con su mes y dia
deacuerdo a lo que el usuario le debe decir que signo del zodiaco es
"""
def run():
    #Tupla para almacenar los signos del zodiaco
    zodiaco = ('Capricornio', 'Acuario', 'Piscis', 'Aries', 'Tauro', 'Geminis', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Escorpio', 'Sagitario')
    #Tupla para almacenar el limite del dia del mes de cada zodiaco
    fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 19)
    try:
        dia = int(input("Ingresa tu dia de nacimiento: "))
        mes = int(input("Ingresa el mes de tu nacimiento: "))
        mes = mes-1 #Restamos para no salirnos de los elementos de la tupla de 0 a 11
        if dia > fechas[mes]:#Evaluamos si dia es mayor a fechas dentro de la posicion de mes, entonces el valor de mes quedaria igual
            mes=mes+1
        if mes==12:
            mes=0 #seria igual a capricornio que seria el primer mes
        print ("Tu signo es: " + zodiaco[mes])
    except ValueError:
        print("Ingresa solo caracteres numericos!")
if __name__ == '__main__':
    bienvenido = "🤗Bienvenido, a descubrir que signo zodiacal eres!😃"
    print(bienvenido)
    run()