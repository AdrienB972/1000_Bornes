#coding:utf-8

class Pile :

    def __init__(self) :
        self.donnees = []

    def empiler (self, element) :
        self.donnees.append(element)

    def depiler (self) :
        return self.donnees.pop()

    def vider (self) :
        self.donnees = []

    def hauteur(self) :
        return len(self.donnees)

    def sommet(self) :
        return self.donnees[hauteur()-1]

    def estVide (self) :
        return self.hauteur() == 0

    def __str__(self) :
        return " Pile = {}".format(self.donnees)