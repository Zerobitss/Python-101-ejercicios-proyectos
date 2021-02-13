class Cuenta():
    def __init__ (self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon

# Getters (metodo Get)
    def get_Saldo(self):
        return self.__saldo

    def get_Propietario(self):
        return self.__propietario

    def get_Moneda(self):
        return self.__moneda

# Setters (metodo Set)

    def set_Moneda(self, moneda):
        self.__moneda = moneda

def run():

    cuenta1 = Cuenta("Zero", 1000, "Dolares")
    print(cuenta1.get_Saldo())
    print(cuenta1.get_Moneda())
    cuenta1.set_Moneda("Bolivares")
    print(cuenta1.get_Moneda())
    cuenta1.set_Moneda("Euros")
    print(cuenta1.get_Moneda())

if __name__ == "__main__":
    run()