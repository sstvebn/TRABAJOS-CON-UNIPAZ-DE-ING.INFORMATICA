SMLV = 1700000  


class Empleado:
    def __init__(self, identificacion, nombre, rol):
        self.identificacion = identificacion
        self.nombre = nombre
        self.rol = rol

    def mostrar_info(self):
        print(f"\n INFORMACIÓN DEL EMPLEADO")
        print(f"Identificación: {self.identificacion}")
        print(f"Nombre: {self.nombre}")
        print(f"Rol: {self.rol}")

class Gerente(Empleado):
    def __init__(self, identificacion, nombre, horas_trabajo):
        super().__init__(identificacion, nombre, rol="Gerente")
        self.salario = 3 * SMLV

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Salario: ${self.salario:,.0f} COP")

    def dirigir(self):
        print(f" {self.nombre} está gestionando al personal y supervisando tareas clave.")

class EmpleadoOrdinario(Empleado):
    def __init__(self, identificacion, nombre, horas_trabajo):
        super().__init__(identificacion, nombre, rol="Empleado Ordinario")
        self.salario = 2 * SMLV
        self.horas_trabajo = horas_trabajo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Salario: ${self.salario:,.0f} COP")
        print(f"Horas de trabajo semanales: {self.horas_trabajo}")

    def trabajar(self):
        print(f"{self.nombre} está cumpliendo con sus {self.horas_trabajo} horas de trabajo semanales.")


gerente = Gerente(identificacion=2001, nombre="Laura Gómez", horas_trabajo=45)
empleado_ordinario = EmpleadoOrdinario(identificacion=3001, nombre="Carlos Pérez", horas_trabajo=40)

gerente.mostrar_info()
empleado_ordinario.mostrar_info()

gerente.dirigir()
empleado_ordinario.trabajar()