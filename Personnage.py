import random

class Personnage:
    def __init__(self):
        self.endurance = random.randint(12, 24)
        self.agilite = random.randint(2, 12)

    def lancer_de(self):
        de = random.randint(2, 12)
        return de

    def soustraire_endurance(self, valeur):
        self.endurance -= valeur
        if self.endurance < 0:
            self.endurance = 0

    def test_agilite(self):
        de = self.lancer_de()
        return de < self.agilite
