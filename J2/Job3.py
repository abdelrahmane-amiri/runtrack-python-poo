class Livre:
    def __init__(self,titre,auteur,pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_pages(self):
        return self.__pages
        
    def set_livre(self,ntitre,nauteur,npages):
        self.__titre = ntitre
        self.__auteur = nauteur
        if isinstance(npages, int) and npages > 0:
            self.__pages = npages
        else:
            self.__pages = str("Erreur de nombre")

    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu.")
        else:
            print(f"Le livre '{self.__titre}' n'avait pas été emprunté.")

    
livre = Livre("Rachid et les 40 voleurs","Abdel",50)
print(livre.get_titre())
print(livre.get_auteur())
print(livre.get_pages())
livre.set_livre("Mort de kai",'Rachid',60)
print(livre.get_titre())
print(livre.get_auteur())
print(livre.get_pages())


livre.emprunter()
livre.rendre()
