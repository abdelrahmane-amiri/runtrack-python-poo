class Rectangle:
    def __init__(self,longeur,largeur):
        self.__longeur = longeur
        self.__largeur = largeur

    def get_valeur(self):
        return self.__longeur
    
    def get_valeur2(self):
        return self.__largeur
    
    def set_valeur(self, nlongeur, nlargeur):
        self.__longeur = nlongeur
        self.__longeur = nlargeur

rectangle = Rectangle(10,20)
print(rectangle.get_valeur())
print(rectangle.get_valeur2())

rectangle.set_valeur(40,40)

print(rectangle.get_valeur())
print(rectangle.get_valeur2())