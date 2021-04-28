from ClaseHumano import Humano


class Orco:

    def __init__(self, nombre, armadura, nivel, ataque):
        self.ojos = 2
        self.piernas = 2
        self.dientes = 56
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = 100



    def atacarr(Humano, self):
        daño = self.ataque - Humano.armadura
        humano_vida = Humano.salud - daño
        print (f"Has atacado al enemigo por {daño} pts de daño, le queda {humano_vida} pts de vida!")
 
    def no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def show_stats(self):
        print(f"Nombre: {self.nombre}| ojos: {self.ojos}| dientes: {self.dientes}| piernas: {self.piernas}| armadura: {self.armadura}| ataque: {self.ataque}| salud: {self.salud}")


zugzug = Orco(nombre = "Zugzug", armadura = 5, nivel = 80, ataque = 36)
