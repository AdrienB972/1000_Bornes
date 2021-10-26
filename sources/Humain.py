#coding:utf-8
import pickle
from Joueur import *

class Humain (Joueur) :
    
    def __init__(self, nom) :
        super().__init__(nom)

    def who(self) :
        return "Humain"

    def jouerTour(self, listeJoueurs, defausse, pioche) :
        cartejouee = False

        # Le joueur tire une une carte dans la pioche
        print("Vous piochez une carte.")
        self.piocher(pioche)

        print("Votre score : " + str(self.score))
        print("Les cartes attaques contre vous : " + str(self.bataille) + " , " + str(self.vitesse))
        chaine = "Vos immunités : ["
        for i in range(0, len(self.immunites)) :
            if i == 1 :
                chaine += ", "
            chaine += str(self.immunites[i])
        chaine += " ]"
        print(chaine)

        # On affiche la main du joueur avec les numéros des cartes pour faciliter le choix
        self.afficherMain()
        
        while ( not cartejouee) :
            saisie = self.choix(0)

            # Dans le cas ou le joueur a saisie "p", on arrete le tour
            if saisie == -1 :
                cartejouee = True

            else :
                carteajouer = self.main[saisie]
                cartejouee = self.jouerCarte(carteajouer, listeJoueurs, defausse)

        while len(self.main) > 6 :
            saisie = self.choix(1)
            self.defausser(self.main[saisie], defausse)



    def attaquer(self, carteajouer, listeJoueurs) :
        valide = False
        print("Quelle joueur voulez vous attaquer ?")
        for i in range(0, len(listeJoueurs)) :
            joueurCible = listeJoueurs[i]
            if not(joueurCible == self ) and (joueurCible.bataille == None) :
                chaine = "Vos immunités : ["
                for i in range(0, len(self.immunites)) :
                    if i == 1 :
                        chaine += ", "
                    chaine += str(self.immunites[i])
                chaine += " ]"
                print("   {} | Nom : {}, Score : {}, bataille : {}, bottes : {}, vitesse : {}".format(i, joueurCible.nom,joueurCible.score, str(joueurCible.bataille), chaine, str(joueurCible.vitesse )))
        while not(valide) :
            saisie = input("Entrez le numéro du joueur : ")
            if saisie.isnumeric() :
                saisie = int(saisie)
                if saisie >= 0 and saisie < len(listeJoueurs) and not(self==(listeJoueurs[saisie])) :
                    joueurCible = listeJoueurs[saisie]
                    if joueurCible.bataille == None :
                        immunisé = False
                        for i in range(0, len(joueurCible.immunites)) :
                            if (joueurCible.immunites[i].effet == carteajouer.effet) :
                                immunisé = True
                        if not immunisé :
                            valide = True
                            joueurCible.bataille = carteajouer
                            self.main.remove(carteajouer)
                        else :
                            print("Ce joueur est immunisé.")
                    else :
                        print("Ce joueur est déja attaqué.")
                else :
                    print("Saisie invalide.")
            else :
                print("Saisie invalide.")

    """
    Plusieurs action selon la valeur entrée en paramêtre :
    Quand action = 0. Retourne le numéro de carte qu'on souhaite jouer ou -1 si "p" est saisie
    Quand action = 1. Retourne le numéro de carte qu'on souhaite jeter
    """
    def choix(self, action) :

        valide = False
        
        if action == 0 :
            
            print("Tapez le numéro de la carte que vous voulez jouer, \"p\" si vous souhaiter passer votre tour : ")
            while(not valide) :
                # Récupération de la saisie rentrée dans la console
                saisie = input()

                # Si le joueur ne souhaite pas jouer, la saise n'est plus demandée
                if saisie==("p") :
                    valide = True
                    return -1

                # Si la saisie est un entier...
                if saisie.isnumeric() :
                    saisie = int(saisie)
                    # Verification si la saisie correspond à un numéro de carte
                    if saisie >= 0 and saisie < len(self.main) :
                        valide = True
                    else :
                        print("Ce numéro ne correspond à aucune carte. Tapez le numéro de la carte que vous voulez jouer.")
                else :
                    print("Commande non valide. Tapez le numéro de la carte que vous voulez jouer.")

            return saisie

        else :

            # On affiche la main du joueur avec les numéros des cartes pour faciliter le choix
            self.afficherMain()
            print("Quelle carte voulez-vous jeter ? Tapez le numéro de la carte que vous voulez jeter.")
            
            while( not valide) :
                # Récupération de la saisie rentrée dans la console
                saisie = input()

                # Si la saisie est un entier
                if saisie.isnumeric() :
                    saisie =int(saisie)
                    # Verification que la saisie correspond bien à l'index d'une carte
                    if saisie >= 0 and saisie < len(self.main) :
                        valide = True
                    else :
                        print("Ce numéro ne correspond à aucune carte. Tapez le numéro de la carte que vous voulez jeter.")
                else :
                    print("Commande non valide. Tapez le numéro de la carte que vous voulez jeter.")
            
            return saisie