class Voiture:
    def __init__(self,marque,modele,annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 4

    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_marche(self):
        return self.__en_marche
    
    def get_reservoir(self):
        return self.__reservoir
    
   
    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def demarrer(self):
        if self.verifier_plein() >= 5:
            self.__en_marche = True

    def arreter(self):
        self.__en_marche = False

    def verifier_plein(self):
        return self.__reservoir
    

voiture = Voiture("Toyota", "Corolla", 2020, 10000)
print(f"Marque: {voiture.get_marque()}")
print(f"Modèle: {voiture.get_modele()}")
print(f"Année: {voiture.get_annee()}")
print(f"Kilométrage: {voiture.get_kilometrage()}")
print(f"En marche: {voiture.get_marche()}")
print(f"Réservoir: {voiture.get_reservoir()}")

voiture.demarrer()
print(f"En marche après démarrage: {voiture.get_marche()}")

voiture.arreter()
print(f"En marche après arrêt: {voiture.get_marche()}")