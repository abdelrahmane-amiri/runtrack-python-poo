class Ville:
    def __init__(self,nom,nombre_habitant):
        self.__nom = nom
        self.__nombre_habitant = nombre_habitant

    def ajouter_habitant(self):
        self.__nombre_habitant += 1

    def get_nom(self):
        return self.__nom

    def get_habitant(self):
        return self.__nombre_habitant


class Personne:
    def __init__(self,nom,age,ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.ajouter_habitant()



paris = Ville("Paris", 55000)
marseille = Ville("Marseille", 861635)

print(f"Nombre d'habitants de Paris : {paris.get_habitant()}")
print(f"Nombre d'habitants de Marseille : {marseille.get_habitant()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print("\nAprès ajout des nouvelles personnes :")
print(f"Nombre d'habitants de Paris : {paris.get_habitant()}")
print(f"Nombre d'habitants de Marseille : {marseille.get_habitant()}")