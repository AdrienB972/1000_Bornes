#coding:utf-8

import random
import pickle
from Pile import *
from Carte import *

class Partie :

    def __init__(self, listeJoueurs) :
        self.listeJoueurs = listeJoueurs
        self.pioche = Pile()
        self.defausse = Pile()
        self.estTerminee = False
        self.joueurCourant = listeJoueurs[0]
        self.positionJoueurCourant = 0

    def distributionCartes(self) :

        # Création et ajout des cartes attaques dans la pioche
        type = 0

        # 5 cartes "feu rouge"
        effet = 1
        for i in range(0, 5) :
            self.pioche.empiler(Carte(type, effet))
        
        # 4 cartes "limite de vitesse"
        effet = 2
        for i in range(0, 4) :
            self.pioche.empiler(Carte(type, effet))

        # 3 cartes "pannes d'essence", "crevaison" et "accident"
        for i in range(0, 3) :
            effet += 1
            for j in range(0, 3) :
                self.pioche.empiler(Carte(type, effet))

        # Création et ajout des cartes parades dans la pioche
        type = 1

        # 14 cartes "feu vert"
        effet = 1
        for i in range(0, 14) :
            self.pioche.empiler(Carte(type, effet))

        # 6 cartes "fin de limite", "essence", "roue de secours" et "reparation"
        for i in range(0, 4) :
            effet += 1
            for j in range(0, 6) :
                self.pioche.empiler(Carte(type, effet))

        # Création et ajout des cartes bottes dans la pioche
        type = 2

        # 1 carte "prioritaire", "citerne", "increvable" et "as du volant"
        effet = 2
        for i in range(0, 4) :
            self.pioche.empiler(Carte(type, effet))
            self.pioche.empiler(Carte(type, effet))
            self.pioche.empiler(Carte(type, effet))
            effet += 1

        # Création et ajout des cartes bornes dans la pioche
        type = 3

        # 10 cartes "25", "50" et "75"
        effet = 1
        for i in range(0, 3) :
            for j in range(0, 10) :
                self.pioche.empiler(Carte(type, effet))
            effet += 1

        # 12 cartes "100"
        for i in range(0, 12) :
            self.pioche.empiler(Carte(type, effet))
        
        # 4 cartes "200"
        effet += 1
        for i in range(0, 4) :
            self.pioche.empiler(Carte(type, effet))

        # Mélange de la pioche
        """
        la fonction shuffle du module random permet de melanger les éléments d'une liste de façon aléatoire
        """
        random.shuffle(self.pioche.donnees)

        # Distribution des cartes aux listeJoueurs
        for i in range(0, len(self.listeJoueurs)) :
            for j in range(0, 6) :
                self.listeJoueurs[i].piocher(self.pioche)

    def lancerPartie(self) :
        while not(self.estTerminee) :
            for i in range(0, len(self.listeJoueurs)) :
                self.positionJoueurCourant = i
                print("------------------------------------------------------------")
                # Si la pioche est vide, on retourne le joueur ayant le plus gros score
                if self.pioche.estVide() :
                    return meilleurJoueur(listeJoueurs)

                # Initialisation nécéssaire pour le tour de chaque joueur
                self.joueurCourant = self.listeJoueurs[i]
                print("C'est au tour de {} !!".format(self.joueurCourant.nom))
                self.joueurCourant.jouerTour(self.listeJoueurs, self.defausse, self.pioche)
                # Si le joueur a atteint 1000 bornes exactement, la partie est terminée
                if self.joueurCourant.score == 1000 :
                    self.estTerminee = True
                    break

                # Sauvegarde de la partie
                self.sauvegarder()

        return self.joueurCourant

    def meilleurJoueur(self, listeJoueurs) :
        meilleur = listeJoueurs[0]
        for i in listeJoueurs:
            if i.score > meilleur.score:
                meilleur = i
        return meilleur

    def sauvegarder(self) :
        with open('./sauvegarde', 'wb') as f :
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
    
    @property
    def listeJoueurs(self) :
        return self.__listeJoueurs

    @property
    def pioche(self) :
        return self.__pioche

    @property
    def defausse(self) :
        return self.__defausse

    @property
    def estTerminee(self) :
        return self.__estTerminee

    @property
    def joueurCourant(self) :
        return self.__joueurCourant

    @listeJoueurs.setter
    def listeJoueurs(self, listeJoueurs) :
        self.__listeJoueurs = listeJoueurs

    @pioche.setter
    def pioche(self, pioche) :
        self.__pioche = pioche

    @defausse.setter
    def defausse(self, defausse) :
        self.__defausse = defausse

    @estTerminee.setter
    def estTerminee(self, estTerminee) :
        self.__estTerminee = estTerminee

    @joueurCourant.setter
    def joueurCourant(self, joueurCourant) :
        self.__joueurCourant = joueurCourant