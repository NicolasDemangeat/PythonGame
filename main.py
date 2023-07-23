from time import sleep

from Joueur import *
from Ennemies import *

joueur = Joueur()
ennemi = Ennemies()

while joueur.endurance > 0 and ennemi.endurance > 0:
    print(f"Vous avez {joueur.endurance} point de vie et {joueur.agilite} d'agilité.")
    print(f"L'ennemi a {ennemi.endurance} point de vie et {ennemi.agilite} d'agilité.")
    input('Jetez les dès pour determiner votre puissance d\'attaque !')
    power_joueur = joueur.throw_dice() + joueur.agilite
    power_ennemi = ennemi.throw_dice() + ennemi.agilite

    print(f'La puissance du joueur est de {power_joueur}')
    print(f'La puissance de l\'ennemi est de {power_ennemi}')
    
    sleep(2)

    if power_joueur > power_ennemi:
        print('Le joueur a gagné cette manche !')
        print("L'ennemi perd 2 points de vie.")
        ennemi.soustraire_endurance(2)
        print(f"Il reste {ennemi.endurance} points de vie a l'ennemi.")
    else:
        print('Le joueur a perdu cette manche !')
        print("Le joueur perd 2 points de vie.")
        joueur.soustraire_endurance(2)
        print(f"Il reste {joueur.endurance} points de vie au joueur.")

print(f"Vous avez {joueur.endurance} point de vie.")
print(f"L'ennemi a {ennemi.endurance} point de vie.")