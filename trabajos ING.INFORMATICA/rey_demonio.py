class Personaje:
    def __init__(self, nombre, titulo, oficio, vidas, tipo_arma, nivel_poder, dano_individual,
                 velocidad, resistencia, magia, regeneracion, intelecto, lealtad=None):
        self.nombre = nombre
        self.titulo = titulo
        self.oficio = oficio
        self.vidas = vidas
        self.tipo_arma = tipo_arma
        self.nivel_poder = nivel_poder
        self.dano_individual = dano_individual
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.magia = magia
        self.regeneracion = regeneracion
        self.intelecto = intelecto
        self.lealtad = lealtad
        self.equipo_especial = []
        self.habilidades = []

    def agregar_equipo(self, equipo):
        self.equipo_especial.append(equipo)

    def agregar_habilidad(self, habilidad):
        self.habilidades.append(habilidad)

    def mostrar_info(self):
        print(f"\n=== {self.nombre} | {self.titulo} ===")
        print(f"Oficio: {self.oficio}")
        print(f"Vidas disponibles: {self.vidas}")
        print(f"Tipo de arma: {self.tipo_arma}")
        print(f"Nivel de poder: {self.nivel_poder}/100")
        print(f"Daño individual: {self.dano_individual}")
        print(f"Velocidad: {self.velocidad}/100")
        print(f"Resistencia: {self.resistencia}/100")
        print(f"Magia: {self.magia}/100")
        print(f"Regeneración: {self.regeneracion}/100")
        print(f"Intelecto estratégico: {self.intelecto}/100")
        if self.lealtad is not None:
            print(f"Lealtad: {self.lealtad}/100")
        print("\n--- Equipo Especial ---")
        for item in self.equipo_especial:
            print(f"- {item}")
        print("\n--- Habilidades ---")
        for hab in self.habilidades:
            print(f"- {hab}")


rey_demonio = Personaje(
    nombre="Asta",
    titulo="Devastador de Reinos Carmesí",
    oficio="Conquistador dimensional absoluto",
    vidas=6,
    tipo_arma="Guantelete Abismal triple núcleo",
    nivel_poder=99,
    dano_individual=2500000,
    velocidad=85,
    resistencia=100,
    magia=98,
    regeneracion=97,
    intelecto=96
)

rey_demonio.agregar_equipo("Corona de la Extinción Primordial")
rey_demonio.agregar_equipo("Manto de Oscuridad Eterna")
rey_demonio.agregar_equipo("Guantelete Abismal")
rey_demonio.agregar_equipo("Talismán del Fin de Ciclo")

rey_demonio.agregar_habilidad("Apocalipsis Carmesí")
rey_demonio.agregar_habilidad("Dominio Abismal")
rey_demonio.agregar_habilidad("Renacimiento Demoníaco")
rey_demonio.agregar_habilidad("Ocultación de Presencia Suprema")
rey_demonio.agregar_habilidad("Sello de Ragnarok")

subdito = Personaje(
    nombre="Kei",
    titulo="Lanza de la Devoción Oscura",
    oficio="Capitán del escuadrón ejecutor del trono infernal",
    vidas=6,
    tipo_arma="Lanza Sacrificial Harkanoros",
    nivel_poder=88,
    dano_individual=1350000,
    velocidad=94,
    resistencia=82,
    magia=60,
    regeneracion=75,
    intelecto=0,
    lealtad=100
)

subdito.agregar_equipo("Armadura de Sangre Purgada")
subdito.agregar_equipo("Lanza Harkanoros")
subdito.agregar_equipo("Brazalete del Juramento Ígneo")
subdito.agregar_equipo("Emblema del Guardián Eterno")

subdito.agregar_habilidad("Impacto Final")
subdito.agregar_habilidad("Velocidad Umbría")
subdito.agregar_habilidad("Escudo de Pacto Infernal")
subdito.agregar_habilidad("Anulación de Técnica")
subdito.agregar_habilidad("Instinto Guardián")

dano_equipo = rey_demonio.dano_individual + subdito.dano_individual
multiplicador_sinergia = 3
dano_final_equipo = dano_equipo * multiplicador_sinergia

tecnica_conjunta = "Eclipse del Reino Infernal"
vidas_consumidas = 1  


print("FICHA COMPLETA DE PERSONAJES")
rey_demonio.mostrar_info()
subdito.mostrar_info()