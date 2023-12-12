from listes_mots import mots
from presentation_regles import intro, difficultes
from fonctions import mot_correct, lettre_correcte
from random import randint

# Présentation des règles du jeu
intro()
# Présentation des différentes difficultés
difficultes()

# L'utilisateur rentre la longueur du mot souhaitée (entre 4 et
# 8 lettres)
taille = int(input(
    "Entrez le nombre de lettres que vous souhaitez (entre 4 et 8): "))
solution = mots[taille-4][randint(0, 25)]
print(solution)

# Lancement du jeu
win = False
while win:
    essai = input("Entrez un mot : ")
    if mot_correct(essai, solution):
        print("Bravo, vous avez trouvé !")
        win = True
    else:
        print("Dommage, ce n'est pas le bon mot. Réessayez.")
