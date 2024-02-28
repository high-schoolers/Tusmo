from listes_mots import mots
from presentation_regles import intro, difficultes
from fonctions import mot_correct, lettre_correcte
from random import randint

def tusmo():
    # Présentation des règles du jeu
    intro()
    # Présentation des différentes difficultés
    diff = difficultes()
    print("Vous aurez",diff,"essais")
    
    # L'utilisateur rentre la longueur du mot souhaitée (entre 4 
    # et 8 lettres)
    taille = int(input("Entrez le nombre de lettres que vous souhaitez (entre 4 et 8): "))
    solution = mots[taille-4][randint(0,25)]

    # Lancement du jeu
    win = False
    tour = 0
    while not win and tour < diff :
        essai = input("Entrez un mot : ")
        if len(essai) != taille :
            print("Taille du mot incorrecte")
            #essai = input("Entrez un mot : ")
        elif mot_correct(essai,solution) == True :
            print("Bravo, vous avez trouvé !")
            win = True
        else :
            print("Dommage, ce n'est pas le bon mot. Réessayez.")
        tour += 1
    if not win :
        print("Nombre d'essais dépassé.")
        print("Le mot était",solution)
    return win
