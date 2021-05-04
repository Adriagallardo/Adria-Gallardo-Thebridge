
class Orco:

    def __init__(self, nombre, nivel, armadura, ataque):
        self.ojos = 2
        self.piernas = 2
        self.dientes = 56
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = 100



    def atacar(self, Humano):
        Humano.salud -= self.ataque - Humano.armadura
        daño_h = self.ataque - Humano.armadura
        print(f'{self.nombre} golpea por {daño_h} pts de daño! La salud del humano {Humano.nombre} es {Humano.salud}')
 
    def no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def show_stats(self):
        print(f"Nombre: {self.nombre}| ojos: {self.ojos}| dientes: {self.dientes}| piernas: {self.piernas}| armadura: {self.armadura}| ataque: {self.ataque}| salud: {self.salud}")


