class Circulo:
    PI = 3.14159  # Definimos una constante

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return Circulo.PI * (self.radio ** 2)

    def circunferencia(self):
        return 2 * Circulo.PI * self.radio

circulo = Circulo(8)

print(f"Área: {circulo.area()}")  
print(f"Circunferencia: {circulo.circunferencia()}") 
