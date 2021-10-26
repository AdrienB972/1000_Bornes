#coding:utf-8

class Carte :

    listeEffets = [["attaque", "feu rouge", "limite de vitesse", "panne d'essence", "crevaison", "accident"],
        ["parade", "feu vert", "fin de limite de vitesse", "essence", "roue de secours", "reparations"],
        ["botte", "prioritaire", "prioritaire", "citerne", "increvable", "as du volant"],
        ["bornes", "25", "50", "75", "100", "200"],
        ["memo","aucun effet"]]

    def __init__(self, type = 4, effet = 1) :
        self.type = type
        self.effet = effet
    
    def __str__(self) :
        return "Carte {} : {}".format(self.listeEffets[self.type][0], self.listeEffets[self.type][self.effet])

    def __eq__(self, objet) :
        if self is objet :
            return True
        if objet == None :
            return False
        if type(self) != type(objet) :
            return False
        if self.type != objet.type :
            return False
        else :
            if self.effet != objet :
                return False

    @property
    def effet(self) :
        return self.__effet

    @property
    def type(self) :
        return self.__type

    @effet.setter
    def effet(self, effet) :
        self.__effet = effet

    @type.setter
    def type(self, type) :
        self.__type = type