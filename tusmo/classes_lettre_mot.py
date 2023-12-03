
class Lettre :
    def __init__(self, etat = 0):
        self.etat = etat
    def lettre_correcte(self,solution,place):
        """Teste si la lettre du mot rentré par l'utilisateur se
        trouve dans le mot-solution et si elle est bien placée

        Paramètres
        ----------
        self : objet de la classe Lettre
        solution : le mot-solution à trouver

        Retourne
        --------
        lettre.etat : le statut de la lettre : absente (0), mal
        placée (1), bien placée (2)
        """
        if self.mot[place] not in solution :
            # la lettre n'est pas dans le mot-solution
            lettre.etat = 0
        else :
            # la lettre est dans le mot-solution
            if self.mot[place] == solution[place]:
                #la lettre est bien placée
                lettre.etat = 2
            else :
                # la lettre est mal placée
                lettre.etat = 1
        return lettre.etat
 
class Mot :
    def __init__(self, mot):    # mot = str
        self.taille = len(mot)
        self.mot = mot
    def __repr__(self):
        return f"{self}"
    def mot_correct(self,solution):
        """Teste si le mot entré par l'utilisateur est correct

        Paramètres
        ----------
        self : objet de la classe Mot
        solution = la solution : le mot correct

        Retourne
        --------
        True si l'utilisateur trouve le bon mot
        False si l'utilisateur n'as pas trouvé le mot
        """
        cnt_correct = 0     # compte le nombre de lettres correctes
        for lettre in self.mot :
            place = 0
            lettre = Lettre()
            if lettre.lettre_correcte(solution,place) == 2 :
                cnt_correct += 1
            place += 1
        if cnt_correct == self.taille :
            return True
        else :
            return False
        
            
# l'utilisateur rentre la longueur du mot souhaitée (entre 4 et
# 8 lettres)
#taille = int(input("Entrez le nombre de lettres que vous souhaitez (entre 4 et 8): "))
solution = Mot("chat")
print(solution)



