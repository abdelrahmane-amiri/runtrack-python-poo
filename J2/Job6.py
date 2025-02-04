class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = {}
        self.__statut = "en cours"

    def ajouter_plat(self, nom_plat, prix):
        if self.__statut == "en cours":
            self.__plats[nom_plat] = prix
        else:
            print("Impossible d'ajouter un plat, la commande est terminée ou annulée.")

    def annuler_commande(self):
        if self.__statut == "en cours":
            self.__statut = "annulée"
            self.__plats.clear()
        else:
            print("Commande déjà terminée ou annulée.")

    def __calculer_total(self):
        return sum(self.__plats.values())

    def calculer_tva(self, taux=0.2):
        return self.__calculer_total() * taux

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande} - Statut: {self.__statut}")
        for plat, prix in self.__plats.items():
            print(f"{plat}: {prix:.2f}€")
        total = self.__calculer_total()
        print(f"Total: {total:.2f}€ | TVA (20%): {self.calculer_tva():.2f}€")


commande = Commande(101)
commande.ajouter_plat("Pizza", 12.5)
commande.ajouter_plat("Salade", 6.0)
commande.afficher_commande()
commande.annuler_commande()
commande.afficher_commande()
