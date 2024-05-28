class Departamento:
    def __init__(self, nombre, gerente):
        self.nombre = nombre
        self.gerente = gerente

    def obtener_gerente(self):
        return self.gerente


class Empleado:
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento

    def obtener_gerente(self):
        return self.departamento.obtener_gerente()

departamento = Departamento("RRHH", "Sr. Hurtado")
empleado = Empleado("Paolo Sosa", departamento)

print(empleado.obtener_gerente())  # Salida: Sr. Hurtado
