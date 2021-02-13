"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa
donde <mes> es el nombre del mes.
"""
def run():
    months = {
    1:'enero',
    2:'febrero',
    3:'marzo',
    4:'abril',
    5:'mayo',
    6:'junio',
    7:'julio',
    8:'agosto',9:'septiembre',
    10:'octubre',
    11:'noviembre',
    12:'diciembre'
    }
    date = input('Introduce una fecha en formato dia/mes/año: ')
    date = date.split('/')
    print(date[0], 'de', months[int(date[1])], 'de', date[2])
if __name__ == "__main__":
    run()