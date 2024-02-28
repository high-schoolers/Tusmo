from time import*
from listes_mots import mots
from presentation_regles import intro, difficultes
from fonctions import mot_correct, lettre_correcte,diff_test,diff4,diff_check
from random import randint


def jeu(tours,solution,diff):
    if diff == 4:
        t = [0]*len(solution)
    win = False
    while win == False:
        print("Tentatives restantes : ",tours)
        while True:
            length = False
            while length == False:
                guess = str(input("Ecrivez un mot : "))
                if len(guess) == len(solution):
                    length = True
                if length == True:
                    break
                else:
                    print(" ")
                    print("Taille incorrecte. Veuillez réesayer.")
                    print(" ")
            good = True
            if diff == 4:
                good = diff_check(guess,solution,t)
            if good == True:
                break
            elif good == False:
                print(" ")
                print("Veuillez mettre les lettres au bon endroit (diffuculté 'Hardcore')")
                print(" ")

            
        if mot_correct(guess,solution) == True:
            win == True
        else:
            tours -= 1
            if diff == 4:
                t = diff4(solution,guess,t)
            if tours == 0:
                break
    return win,tours

intro()
while True:
    diff = difficultes()
    if diff == 1:
        tours = 8
    if diff == 2:
        tours = 6
    if diff == 3 or diff == 4:
        tours = 4
    print("--------------------------------------------------------")
    print("Début du jeu : ")
    print(" ")
    print(" ")
    taille = int(input("Entrez le nombre de lettres que vous souhaitez (entre 4 et 8): "))
    solution = mots[taille-4][randint(0,25)]
    win,tours = jeu(tours,solution,diff)
    if win == True:
        print("Gagné! :)")
        print("Tours restants ->",tours)
    if win == False:
        print("Perdu! Le mot était : ",solution)
    print("Voulez-vous refaire une partie?")
    ans = str(input("Oui ou Non? : "))
    if ans == "non" or ans == "Non" or ans == "NON":
        break
    else:
        print("UwU")
