"""
Haz el objeto de una lavadora
"""
class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Anadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()

# class Geeks:
#      def __init__(self):
#           self._age = 0
       
#      # using property decorator
#      # a getter function
#      @property
#      def age(self):
#          print("getter method called")
#          return self._age
       
#      # a setter function
#      @age.setter
#      def age(self, a):
#          if(a < 18):
#             raise ValueError("Sorry you age is below eligibility criteria")
#          print("setter method called")
#          self._age = a
  
# mark = Geeks()
  
# mark.age = 19
  
# print(mark.age)
# # setter method called
# # getter method called
