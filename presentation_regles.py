from time import*


def intro():
    print("Bonjour! Bienvenue dans le TUSMO. Avez-vous besoin des règles?")
    sleep(0.5)
    ans = str(input("Oui ou Non? "))
    if ans == "oui" or ans == "Oui" or ans == "OUI":
        print("Le TUSMO, aussi connu sous le nom de Wordle, est un jeu où "
              "l'objectif est de deviner un mot.")
        sleep(0.5)
        print("Vous commencez par choisir la longueur du mot, puis vous "
              "mettez votre réponse.")
        sleep(0.5)
        print("La lettre sera grise si elle n'est pas présente dans le mot.")
        sleep(0.5)
        print("Elle sera jaune si elle est presénte mais au mauvais endroit.")
        sleep(0.5)
        print("Elle sera bleue si elle est au bon endroit.")


def difficultes():
    print("Il y a différentes difficultés :")
    sleep(0.5)
    print("Facile : 10 tentatives")
    sleep(0.5)
    print("Moyen : 6 tentatives")
    sleep(0.5)
    print("Difficile : 4 tentatives")
    sleep(0.5)
    print("Hardcore : 4 tentatives. Vous êtes forcé de garder les lettres "
          "déjà trouvées.")
    sleep(0.5)
    while True:
        diff = int(input("Choisissez 1,2,3 ou 4 : "))
        if diff == 1 or 2 or 3 or 4:
            break
    return diff
"""
def jeu(tours):
    while True:
        print("Tentatives restantes : ",tours)
        guess = str(input("Ecrivez un mot : ")
        #if mot_correct(guess) == True:
            #print("Gagné! :)")
            #print("Tours restants -> ",tours)
            #break
        else:  
            tours -= 1
            if tours == 0:
                print("Perdu! Le mot était : ",mot)
                break
intro()
while True:
    diff = difficultés()
    if diff == 1:
        tours = 10
    if diff == 2:
        tours = 6
    if diff == 3 or diff == 4:
        tours = 4
    jeu(tours)
    print("Voulez-vous refaire une partie?")
    ans = str(input("Oui ou Non?"))
    if ans == "non" or ans == "Non" or ans == "NON":
        break
    else:
        print("UwU")
"""
