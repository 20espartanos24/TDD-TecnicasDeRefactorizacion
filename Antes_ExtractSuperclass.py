class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def arrancar(self):
        print(f"{self.marca} {self.modelo} está arrancando")

    def detener(self):
        print(f"{self.marca} {self.modelo} se ha detenido")


class Motocicleta:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def arrancar(self):
        print(f"{self.marca} {self.modelo} está arrancando")

    def detener(self):
        print(f"{self.marca} {self.modelo} se ha detenido")

mi_coche = Coche("Toyota", "Corolla", 2024)
mi_motocicleta = Motocicleta("Yamaha", "MT-07", 2020)

mi_coche.arrancar()
mi_motocicleta.arrancar()

mi_coche.detener()
mi_motocicleta.detener()

