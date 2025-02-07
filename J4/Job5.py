class Forme:

    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def aire(self):
        return self.__longueur * self.__largeur
    
class Cercle(Forme):
    def __init__(self,radius):
        super().__init__()
        self.__radius = radius

    def aire(self):
        return 3.14 * self.__radius * self.__radius
    
   
rectangle = Rectangle(2,5)
print(f"L'aire du rectangle est : {rectangle.aire()}")

cercle = Cercle(5)
print(f"L'aire du cercle est de : {cercle.aire()}")
    