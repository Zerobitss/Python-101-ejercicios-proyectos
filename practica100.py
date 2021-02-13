"""
Hacer que la preparacion tenga un contador de tiempo de 5segundos
"""
import time

"""
def preparation(self, value = None):

    i = 5seg()
    if value == True:
        Empiece a descontar
    for i in iterable():
        print(Tu tiempo restante es: {i})
        if i >= iterable:
            print("Tu pedido esta listo")
            sleep = 1+ seg
    else:
        tiempo ++ 5


"""

class Lunch():
    def __init__(self, total_protein, carbs, grease):
        self.__protein = total_protein
        self.__carbs = carbs
        self.__grease = grease
        print("You have make a lunch")

    def __str__(self):
        return f'Your luch have {self.__protein}, {self.__carbs}, {self.__grease}'

    def __preparation(self):
        pass

    @property
    def decorator(self):
        print("return protein")
        return self.__protein

    @decorator.setter
    def set_decorator(self, value):
        self.__protein = value
        if value > 0:
            print("Setting correctly")

class Meat():
    def __init__(self, types, temp):
        self._type = types
        self._temp = temp

    def __str__(self):
        return f'{self._type}, {self._temp}'

class Hamburguer(Lunch):
    def __init__(self, total_protein, carbs, grease, meat, bread, sauce, vegetals):
        super().__init__(total_protein, carbs, grease)
        self._meat = meat
        self._bread = bread
        self._sauce = sauce
        self._vegetals = vegetals

    def __str__(self):
        return f"Your hamburger is: {self._meat}, {self._bread}, {self._sauce},{self._vegetals}"


class HotDog(Lunch):
    def __init__(self, total_protein, carbs, grease, sausage, bread, fries, vegetals, sauce):
        super().__init__(total_protein, carbs, grease)
        self._sausage = sausage
        self._bread = bread
        self._fries = fries
        self._vegetals = vegetals
        self._sauce = sauce

    def __str__(self):
        return f'{self._sausage}, {self._bread}, {self._fries}, {self._vegetals}, {self._sauce}'


def run():
    hamburguesa = Hamburguer(150, 20, 100, Meat('chicken', 50),"Pan", 'BBQ',["Lettuce", "tomato", "onion"])
    print(f"{hamburguesa}")

    perro = HotDog(100, 10, 70, Meat('Pork', 40), 'Pan normal de perro xd', 'French fries', 'Onion', 'Garlic sauce')
    perro.set_decorator = 1
    print(perro)


if __name__ == "__main__":
    run()