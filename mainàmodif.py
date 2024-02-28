from listes_mots import mots
from presentation_regles import intro, difficultes
from fonctions import mot_correct, lettre_correcte, dessiner_tentative
from random import randint
import sys
import pygame
from pygame.locals import *


pygame.init()
# Initialisation de la fenêtre
largeur_fen = 800
hauteur_fen = 300
fenetre = pygame.display.set_mode((largeur_fen, hauteur_fen))
pygame.display.set_caption("Tusmo")
indice_case = 0

def tusmo():
    # Présentation des règles du jeu
    intro()
    # Présentation des différentes difficultés
    diff = difficultes()
    print("Vous aurez",diff,"essais")
    
    # L'utilisateur rentre la longueur du mot souhaitée (entre 4 
    # et 8 lettres)
    taille = int(input("Entrez le nombre de lettres que vous souhaitez (entre 4 et 8): "))
    if 4 <= taille <= 8:
        solution = mots[taille - 4][randint(0, len(mots[taille - 4]) - 1)]
    else:
        print("La taille du mot est hors de la plage autorisée.")
        return

    # Lancement du jeu
    win = False
    tour = 0
    global tentatives
    tentatives = []

    pygame.display.flip()
    
    while not win and tour < diff:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        essai = input("Entrez un mot : ")
        if len(essai) != taille:
            print("Taille du mot incorrecte")
        elif mot_correct(essai, solution) == True:
            print("Bravo, vous avez trouvé !")
            win = True
        else:
            print("Dommage, ce n'est pas le bon mot. Réessayez.")
            tentatives.append(essai)
            dessiner_tentative(tentatives, solution, taille, diff, fenetre, largeur_fen, hauteur_fen)

        tour += 1

    if not win:
        print("Nombre d'essais dépassé.")
        print("Le mot était", solution)



tusmo()
