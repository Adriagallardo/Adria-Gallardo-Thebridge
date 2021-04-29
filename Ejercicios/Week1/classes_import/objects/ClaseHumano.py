class Humano:

    def __init__(self, nombre, nivel, armadura, ataque):
        self.ojos = 2
        self.piernas = 2
        self.dientes = 32
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = 100
    
    def atacar(self, Orco):
        Orco.salud -= self.ataque - Orco.armadura
        daño_o = self.ataque - Orco.armadura
        print(f'{self.nombre} golpea por {daño_o} pts de daño! La salud del orco {Orco.nombre} es {Orco.salud}')
 
    def no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def show_stats(self):
        print(f"Nombre: {self.nombre} | ojos: {self.ojos} | dientes: {self.dientes} | piernas: {self.piernas} | armadura: {self.armadura} | ataque: {self.ataque} | salud: {self.salud}")

