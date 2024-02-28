import pygame
def lettre_correcte(mot, place, solution):
    """Teste si la lettre du mot rentré par l'utilisateur se
    trouve dans le mot-solution et si elle est bien placée

    Paramètres
    ----------
    mot : string
        le mot entré par l'utilisateur
    place : int
        le rang de la lettre dans le mot
    solution : string
        le mot-solution à trouver

    Retourne
    --------
    Le statut de la lettre : int
        0 si absente, 1 si mal placée, 2 si bien placée
    """
    if mot[place] not in solution:
        # la lettre n'est pas dans le mot-solution
        return 0
    else:
        # la lettre est dans le mot-solution
        if mot[place] == solution[place]:
            # la lettre est bien placée
            return 2
        else:
            # la lettre est mal placée
            return 1


def mot_correct(mot, solution):
    """Teste si le mot entré par l'utilisateur est correct

    Paramètres
    ----------
    mot : string
        le mot rentré par l'utilisateur
    solution : string
        le mot correct

    Retourne
    --------
    True si l'utilisateur trouve le bon mot
    False si l'utilisateur n'as pas trouvé le mot
    """
    cnt_correct = 0     # le nombre de lettres bien placées
    for i in range(len(mot)):
        lettre = lettre_correcte(mot, i, solution)
        print(mot[i], ":", lettre)
        if lettre == 2:
            cnt_correct += 1
    return cnt_correct == len(mot)   

def diff4(solution,guess,t):
    for i in range(len(solution)):
        lettre = solution[i]
        for j in range(len(guess)):
            if guess[j] == guess[i]:
                if guess[j] == lettre:
                    t[i] = 2
                    pass
    return t

def diff_check(guess,solution,t):
    good = True
    for i in range(len(t)):
        if t[i] == 2:
            if guess[i] != solution[i]:
                good = False
    return good

def dessiner_tentative(tentatives, solution, taille, diff, fenetre, largeur_fen, hauteur_fen):
    """Affiche les tentatives du joueur dans la fenetre Pygame

    Paramètres
    ----------
    tentatives : liste de string
        les tentatives du joueur 
    solution : string
        le mot correct
    taille : int
        longueur du mot à trouver
    diff : int
        nombre de tentatives autorisées en fonction de la difficulté du jeu
    largeur_fen : int
        largeur de la fenetre pygame
    hauteur_fen : int
        hauteur de la fenetre pygame
    
    Retourne
    --------
    dessine les tentatives de l'utilisateur sur la fenêtre Pygame,
    en affichant les lettres correctes, mal placées et bien placées
    """
    fenetre.fill((0, 0, 0))
    largeur_case = largeur_fen // taille
    largeur_bordure = 2
    police = pygame.font.Font(None, 36)

    for idx, t in enumerate(tentatives):
        for i, lettre in enumerate(t):  # Utiliser enumerate pour obtenir l'indice correct
            status = lettre_correcte(t, i, solution)  # Utiliser la lettre de la tentative
            color = (255, 255, 255)  # Default color (white)

            if status == 0:
                color = (128, 128, 128)
            elif status == 1:
                color = (255, 255, 0)
            elif status == 2:
                color = (255, 0, 0)

            texte_surface = police.render(lettre, True, (255, 255, 255))

            case_x = i * largeur_case + i * largeur_bordure
            case_rect = pygame.Rect(case_x, idx * (hauteur_fen // diff), largeur_case,
                                    hauteur_fen // diff)

            pygame.draw.rect(fenetre, color, case_rect)  # Utiliser la couleur correcte pour la case
            pygame.draw.rect(fenetre, (255, 255, 255), case_rect, largeur_bordure)  # Dessiner la bordure
            texte_rect = texte_surface.get_rect(center=case_rect.center)
            fenetre.blit(texte_surface, texte_rect)

    pygame.display.flip()
