class Humano:

    def __init__(self, nombre, armadura, nivel, ataque):
        self.ojos = 2
        self.piernas = 2
        self.dientes = 32
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = 100



    def atacar(armadura_orco, self):
        daño = armadura_orco - self.ataque
        orco_vida = 100 - daño
        print (f"Has atacado al enemigo por {daño} pts de daño, le queda {orco_vida} pts de vida!")

adri = Humano(nombre = "Adri", armadura = 20, nivel = 100, ataque = 15)

adri.atacar(armadura_orco = 7)