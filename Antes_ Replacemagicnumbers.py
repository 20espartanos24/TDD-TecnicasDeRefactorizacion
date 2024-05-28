class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * (self.radio ** 2)

    def circunferencia(self):
        return 2 * 3.14159 * self.radio

circulo = Circulo(8)

print(f"Área: {circulo.area()}")  
print(f"Circunferencia: {circulo.circunferencia()}")  
