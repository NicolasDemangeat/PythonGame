import random
from Personnage import Personnage

class Joueur(Personnage):
    def __init__(self):
        super().__init__()
        self.chance = random.randint(2, 12)

    def test_chance(self):
        de = self.lancer_de()
        return de < self.chance

