from Joueur import *
from Ennemies import *

joueur = Joueur()
ennemi = Ennemies()

print(f"Vous avez {joueur.endurance} point de vie.")
print(f"L'ennemi a {ennemi.endurance} point de vie.")

power_joueur = joueur.lancer_de()
power_ennemi = ennemi.lancer_de()

print(f'La puissance du joueur est de {power_joueur}')
print(f'La puissance de l\'ennemi est de {power_ennemi}')

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
    
