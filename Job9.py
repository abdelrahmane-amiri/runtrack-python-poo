class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}, Prix TTC: {self.CalculerPrixTTC()}"

    def changerNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def changerPrix(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def getNom(self):
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA


produit1 = Produit("Produit A", 100, 20)
produit2 = Produit("Produit B", 200, 10)
produit3 = Produit("Produit C", 150, 5)


print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())


produit1.changerNom("Nouveau Produit A")
produit1.changerPrix(120)

produit2.changerNom("Nouveau Produit B")
produit2.changerPrix(220)

produit3.changerNom("Nouveau Produit C")
produit3.changerPrix(180)


print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())
