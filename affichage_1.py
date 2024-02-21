import pygame
import sys

pygame.init()
#initialisation de la fenêtre
largeur_fen=800
hauteur_fen=300
fenetre=pygame.display.set_mode((largeur_fen, hauteur_fen))
pygame.display.set_caption("Tusmo")

taille=8 #la taille du mot
essais=4 #le nombre d'essais possibles

#calcul largeur case
largeur_case=largeur_fen//taille
largeur_bordure=2

#police et taille du texte
police=pygame.font.Font(None, 36)

stock_lettres=[] #liste qui stocke les lettres pressées
stock_essais=[] #liste qui stocke les essais=lignes
indice_case=0 #indice de la case actuelle

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN: #si une touche est pressée on la récupère dans touche
            touche=event.unicode
            if 'a'<=touche<='z' :
                if indice_case<taille:
                    stock_lettres.append(touche)
                    # Créer une surface avec le texte
                    texte=stock_lettres[indice_case]
                    texte_surface=police.render(texte, True, (255, 255, 255))
                    # Calculer la position de la case et dessiner la bordure
                    case_x=indice_case*largeur_case+indice_case*largeur_bordure
                    case_rect=pygame.Rect(case_x, len(stock_essais)*(hauteur_fen//essais), largeur_case, hauteur_fen//essais)
                    fenetre.fill((90,50,255), case_rect)  # Effacer la case
                    pygame.draw.rect(fenetre, (255, 255, 255), case_rect, largeur_bordure)  # Dessiner la bordure
                    # Afficher le texte au centre de la case
                    texte_rect=texte_surface.get_rect(center=case_rect.center)
                    fenetre.blit(texte_surface, texte_rect)
                    pygame.display.flip() #mise à jour de l'affichage
                    indice_case+=1 #passage à la case suivante
                if indice_case==taille: #si toutes les cases de la ligne sont remplies
                    stock_essais.append(stock_lettres.copy())
                    stock_lettres.clear()
                    indice_case=0
            if len(stock_essais)==essais: #si le nombre d'essais est atteint
                pygame.quit()
                sys.exit()
'''
(90,50,255) = bleu bizar = couleur basique
(64,64,64) = gris = lettre pas dans le mot
(255,255,0) = jaune = lettre bien placée
(255,0,0) = rouge = lettre mal placée
'''
