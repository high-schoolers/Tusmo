from listes_mots import mots
from presentation_regles import intro, difficultes
from fonctions import mot_correct, lettre_correcte,diff4,diff_check
from random import randint

def niveau4(tours,solution,diff):
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
            win = True
            break
        else:
            tours -= 1
            if diff == 4:
                t = diff4(solution,guess,t)
            if tours == 0:
                break
    return win

def tusmo():
    # Présentation des règles du jeu
    intro()
    # Présentation des différentes difficultés
    niveau = difficultes()
    nb_essais = niveau[1]
    diff = niveau[0]
    print("Vous aurez",nb_essais,"essais")
    
    # L'utilisateur rentre la longueur du mot souhaitée (entre 4 
    # et 8 lettres)
    taille = int(input("Entrez le nombre de lettres que vous souhaitez (entre 4 et 8): "))
    solution = mots[taille-4][randint(0,25)]
    
    if diff == 4 :
        if niveau4(nb_essais,solution,diff):
            print("Bravo, vous avez trouvé !")
            return True
    
        else :
            print("Nombre d'essais dépassé.")
            print("Le mot était",solution)
            return False
        
    else :
        # Lancement du jeu
        win = False
        tour = 0
        while not win and tour < nb_essais :
            essai = input("Entrez un mot : ")
            if len(essai) != taille :
                print("Taille du mot incorrecte")
            elif mot_correct(essai,solution) == True :
                print("Bravo, vous avez trouvé !")
                win = True
            else :
                if not(tour == nb_essais-1):
                    print("Dommage, ce n'est pas le bon mot. Réessayez.")
            tour += 1
            print("Essais restants :",nb_essais-tour)
        if not win :
            print("Nombre d'essais dépassé.")
            print("Le mot était",solution)
    return win

            
   
