class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self,longueur):
        self.__longueur = longueur

    def set_largeur(self,largeur):
        self.__largeur = largeur


    def perimetre(self):
        return (self.__longueur * 2 + self.__largeur*2)

    def surface(self):
        return (self.__longueur * self.__largeur)

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        return (self.get_longueur() * self.get_largeur() * self.hauteur)

rectangle = Rectangle(2,2)
print(f"Le perimètre du rectangle est : {rectangle.perimetre()} cm ")
print(f"La surface du rectangle est : {rectangle.surface()} cm²")

para = Parallelepipede(2,2,2)

print(f"Le volume du Parallelepipede est de : {para.volume()}")