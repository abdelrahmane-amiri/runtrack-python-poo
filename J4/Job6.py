class Vehicule:
    def __init__(self,marque,modele,annee,prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationVehicule(self):
        print(f"Marque : {self.marque}\nModèle : {self.modele}\nAnnee : {self.annee}\nPrix : {self.prix}")

    def demarrer(self):
        print("Attention, je roule")
        
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationVehicule(self):
        super().informationVehicule()
        print(f"Portes : {self.portes}")

    def demarrer(self):
        print("Attention, La voiture roule")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue = 2):
        super().__init__(marque, modele, annee, prix)
        self.roue = roue

    def informationVehicule(self):
        super().informationVehicule()
        print(f"Roue : {self.roue} ")

    def demarrer(self):
        print("Attention, La moto roule")

dacia = Voiture("Dacia",3008,2011,7000)
dacia.informationVehicule()
dacia.demarrer()

moto = Moto("Tmax","200",2024,10000)
moto.informationVehicule()
moto.demarrer()