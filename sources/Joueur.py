#coding:utf-8
from abc import ABC, abstractmethod
from Carte import *

class Joueur(ABC) :

    def __init__(self, nom) :
        self.nom = nom
        self.score = 0
        self.main = []
        self.peutRouler = False
        self.bataille = None
        self.vitesse = None
        self.immunites = []

    def piocher(self, pioche) :
        self.main.append(pioche.depiler())

    def defausser(self, carte, defausse) :
        defausse.empiler(carte)
        self.main.remove(carte)

    def jouerCarte(self, carte, listeJoueurs, defausse) :
        typecarte = carte.type
        possible = False

        # Si la carte jouée est une carte Attaque
        if typecarte == 0 :

            # Vérification de la possibilité d'attaquer un joueur adverse
            if self.peutAttaquer(carte, listeJoueurs) :
                possible = True
                self.attaquer(carte, listeJoueurs)

            else :
                print("Personne ne peut être attaqué")
            
        # Si la carte jouée est une carte Parade
        if typecarte == 1 :

            """
            Vérification de l'utilisation d'une carte "feu vert".
			Deux utilisations possibles selon qu'on soit en début de partie
			ou après avoir démarré au moins une fois.
            """
            if not(self.peutRouler) and carte.effet == 1 :
                possible = True
                self.peutRouler = True
                defausse.empiler(self.bataille)
                defausse.empiler(carte)
                self.bataille = None
                self.main.remove(carte)

            else :
                # Verification que le joueur à été attaqué
                if (self.bataille != None) or (self.vitesse != None) :

                    # Vérification de la correspondance entre la carte attaque et la carte parade
                    if self.bataille != None and self.bataille.effet == carte.effet :
                        possible = True
                        self.peutRouler = True
                        defausse.empiler(self.bataille)
                        defausse.empiler(carte)
                        self.bataille = None
                        self.main.remove(carte)
                    else :
                        if self.vitesse != None and self.vitesse.effet == carte.effet :
                            possible = True
                            self.peutRouler = True
                            defausse.empiler(self.bataille)
                            defausse.empiler(carte)
                            self.bataille = None
                            self.main.remove(carte)
                else :
                    print("Vous n'avez pas été attaqué !")

        # Si la carte jouée est une carte Botte
        if typecarte == 2 :

            # Utilisation en preventif
            if(len(self.immunites) != 2) :
                possible = True
                self.immunites.append(carte)
                self.main.remove(carte)
            else :
                print("Vous disposez déjà de deux bottes.")

        # Si la carte jouée est une carte Borne
        if typecarte == 3 :

            # Verification qu'un feu vert a deja été posé au moins une fois
            if self.peutRouler :

                # Verification qu'aucune attaque ne bloque l'avancement
                if self.bataille == None :
                    
                    # Vérification de limite de vitesse
                    if self.vitesse != None :
                        if int(Carte.listeEffets[3][carte.effet]) <= 50 :
                            possible = True
                            points = int(Carte.listeEffets[3][carte.effet])
                            self.score += points
                            self.main.remove(carte)
                        else :
                            print("Vous ête limité à 50")
                    else :
                        if self.score + int(Carte.listeEffets[3][carte.effet]) > 1000 :
                            print("Vous ne pouvez pas dépasser mille bornes !")
                        else :
                            possible = True
                            points = int(Carte.listeEffets[3][carte.effet])
                            self.score += points
                            self.main.remove(carte)
                else :
                    print("Vous avez été attaqué ! Jouez une carte parade !")
            else :
                print("Vous êtes à l'arrêt ! Jouez une carte feu vert pour rouler !")

        return possible


    """
    Retourne si le joueur peut utiliser une carte de type attaque
    """
    def peutAttaquer(self, carte, listeJoueurs) :
        peutAttaquer = False
        joueur = None

        i = 0
        while not(peutAttaquer) and i < len(listeJoueurs) :
            if not (self == listeJoueurs[i]) :
                joueur = listeJoueurs[i]
                if joueur.peutRouler :
                    if joueur.bataille == None :
                        if len(joueur.immunites) != 0 :
                            peutAttaquer = True
                            k = 0
                            while k < len(joueur.immunites) :
                                if (joueur.immunites[k].effet == carte.effet) :
                                    peutAttaquer = False
                                k += 1
                        else :
                            peutAttaquer = True
            i += 1

        return peutAttaquer


    def afficherMain(self) :
        print("Cartes en main :")
        for i in range(0, len(self.main)) :
            print("   {} | {}".format(i, self.main[i]))


    def __eq__(self, objet) :
        if (self is objet) :
            return True
        if objet == None :
            return False
        if type(self) != type(objet) :
            return False
        if self.bataille == None :
            if (objet.bataille != None) :
                return False
        else :
            if not(self.bataille == objet.bataille) :
                return False
        if self.peutRouler != objet.peutRouler :
            return False
        if self.immunites == None :
            if objet.immunites != None :
                return False
        else :
            if not(self.immunites == objet.immunites) :
                return False
        if self.main == None :
            if objet.main != None :
                return False
        else :
            if not(self.main == objet.main) :
                return False
        if self.nom == None :
            if objet.nom != None :
                return False
        else :
            if not(self.nom == objet.nom) :
                return False
        if self.score != objet.score :
            return False
        if self.vitesse == None :
            if objet.vitesse != None :
                return False
        else :
            if not(self.vitesse == objet.vitesse) :
                return False
        return True

    def __str__(self) :
        return "{} [nom = {}, score = {}, main = {}, peutRouler = {}, bataille = {}, vitesse = {}, immunites = {}".format(self.who(), self.nom, self.score, self.main, self.peutRouler, self.attaque, self.vitesse, self.immunites)

    @abstractmethod
    def who(self) :
        pass

    @abstractmethod
    def jouerTour (self, carte, defausse) :
        pass

    @property
    def nom(self) :
        return self.__nom

    @property
    def score(self) :
        return self.__score

    @property
    def main(self) :
        return self.__main

    @property
    def peutRouler(self) :
        return self.__peutRouler
    
    @property
    def bataille(self) :
        return self.__bataille

    @property
    def vitesse(self) :
        return self.__vitesse

    @property
    def immunites(self) :
        return self.__immunites

    @nom.setter
    def nom(self, nom) :
        self.__nom = nom

    @score.setter
    def score(self, score) :
        self.__score = score

    @main.setter
    def main(self, main) :
        self.__main = main

    @peutRouler.setter
    def peutRouler(self, peutRouler) :
        self.__peutRouler = peutRouler

    @bataille.setter
    def bataille(self, bataille) :
        self.__bataille = bataille

    @vitesse.setter
    def vitesse(self, vitesse) :
        self.__vitesse = vitesse

    @immunites.setter
    def immunites(self, immunites) :
        self.__immunites = immunites