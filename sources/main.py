# coding:utf-8
# Programme principal
# C'est ce fichier qui lancera l'execution du jeu

from Humain import *
from Joueur import *
from Pile import *
from Carte import *
from Partie import *
	

print("------------------------------------------------------------")
print("1000 Bornes".center(60))
print("------------------------------------------------------------")
print()

# Cette fonction est utile pour charger le fichier de sauvegarde
def charger() :
        with open('./sauvegarde', 'rb') as f :
            return pickle.load(f)

lance = True

while lance :

    saisie = input("Voulez vous charger la dernière sauvegarde ? o/n : ")

    if saisie == "n" :

        valide1 = False
        while not valide1 :
            listeJoueurs = []
            nbJoueurs = int(input("Entrer le nombre de joueurs (2 à 4) : "))
            if nbJoueurs < 2 or nbJoueurs > 4:
                print("Nombre de joueurs incorrect. Entrer 2, 3 ou 4 joueurs")
            else :
                valide1 = True

        for i in range(1, nbJoueurs+1) :
            nomJoueur = str(input("Entrer le nom du Joueur {} : ".format(i)))
            j = Humain(nomJoueur)
            listeJoueurs.append(j)
            
        p = Partie(listeJoueurs)
        p.distributionCartes()

    elif saisie == "o" :

        p = charger()

    else :
        break

    joueurGagnant = p.lancerPartie()

    print()
    print("{} a atteint {} bornes et a gagné(e) la partie !!".format(joueurGagnant.nom, joueurGagnant.score))
    print("Bien joué {} !".format(joueurGagnant.nom))
    print("------------------------------------------------------------")
    saisie = input("Voulez vous relancer la partie ? o/n : ")

    valide2 = False
    while not valide2 :
        if str(saisie) == "o" :
            lance = True
            valide2 = True

        if str(saisie) == "n" :
            lance = False
            valide2 = True