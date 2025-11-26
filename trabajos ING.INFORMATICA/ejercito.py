class Miembro:
    def __init__(self, identificacion: str, nombre: str, rango: str, peloton: str):
        self._identificacion = identificacion   
        self.nombre = nombre
        self.rango = rango
        self.peloton = peloton

    def identificar(self):
        return self._identificacion

    def describir(self):
        return f"ID: {self.identificar()} | {self.rango} {self.nombre} - Pelotón: {self.peloton}"


class SoldadoRaso(Miembro):
    def __init__(self, identificacion, nombre, peloton, alias, edad, especialidad, rango_habilidad, tiempo_servicio_a_prestar, estado_servicio):
        super().__init__(identificacion, nombre, "Soldado Raso", peloton)
        self.alias = alias
        self.edad = edad
        self.especialidad = especialidad
        self.rango_habilidad = rango_habilidad
        self.tiempo_servicio_a_prestar = tiempo_servicio_a_prestar
        self.estado_servicio = estado_servicio  

    def describir(self):
        base = super().describir()
        return (
            f"{base} | Alias: {self.alias} | Edad: {self.edad} años | "
            f"Especialidad: {self.especialidad} | Nivel de habilidad: {self.rango_habilidad} | "
            f"Tiempo por prestar: {self.tiempo_servicio_a_prestar} | Estado: {self.estado_servicio}"
        )


class Cabo(Miembro):
    def __init__(self, identificacion, nombre, peloton, tiempo_servicio_prestado):
        super().__init__(identificacion, nombre, "Cabo", peloton)
        self.tiempo_servicio_prestado = tiempo_servicio_prestado

    def describir(self):
        base = super().describir()
        return f"{base} | Tiempo servido: {self.tiempo_servicio_prestado}"


class Sargento(Miembro):
    def __init__(self, identificacion, nombre, peloton, peloton_a_cargo):
        super().__init__(identificacion, nombre, "Sargento", peloton)
        self.peloton_a_cargo = peloton_a_cargo

    def describir(self):
        base = super().describir()
        return f"{base} | A cargo del pelotón: {self.peloton_a_cargo}"


class Teniente(Miembro):
    def __init__(self, identificacion, nombre, peloton, numero_oficiales_a_cargo):
        super().__init__(identificacion, nombre, "Teniente", peloton)
        self.numero_oficiales_a_cargo = numero_oficiales_a_cargo

    def describir(self):
        base = super().describir()
        return f"{base} | Oficiales a su cargo: {self.numero_oficiales_a_cargo}"


class General(Miembro):
    def __init__(self, identificacion, nombre, peloton, batallon_a_cargo):
        super().__init__(identificacion, nombre, "General", peloton)
        self.batallon_a_cargo = batallon_a_cargo

    def describir(self):
        base = super().describir()
        return f"{base} | Batallón a su cargo: {self.batallon_a_cargo}"


miembros = [
    SoldadoRaso(
        "ID001", "Juan Pérez", "Pelotón A", alias="El Halcón", edad=23,
        especialidad="Francotirador", rango_habilidad="Avanzado",
        tiempo_servicio_a_prestar="12 meses", estado_servicio="Activo"
    ),
    Cabo("ID002", "Luis Gómez", "Pelotón A", tiempo_servicio_prestado="2 años"),
    Sargento("ID003", "María Torres", "Pelotón B", peloton_a_cargo="Pelotón B"),
    Teniente("ID004", "Carlos Ramírez", "Pelotón C", numero_oficiales_a_cargo=6),
    General("ID005", "Ana Morales", "Cuartel Central", batallon_a_cargo="Batallón Nº7"),
]


for m in miembros:
    print(m.describir())