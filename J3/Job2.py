class CompteBanquaire:
    def __init__(self,id,nom,prenom,solde):
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = True

    def get_id(self):
        return self.__id
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde


    def afficher(self):
        print(f"ID : {self.get_id()}")
        print(f"Nom : {self.get_nom()}")
        print(f"Prenom : {self.get_prenom()}")

    def afficher_solde(self):
        print(f"Solde : {self.get_solde()}")

    def versement(self,chiffre):
        self.__solde += chiffre

    def retrait(self,chiffre):
        if self.__decouvert:          
            self.__solde -= chiffre
            print(f"Solde : {self.get_solde()}")
        else:
            if (self.__solde - chiffre) >= 0:
                self.__solde -= chiffre
                print(f"Solde : {self.get_solde()}")
            else:
                print("Vous n'avez pas assez sur le compte")
    
    def agios(self,chiffre):
        if self.get_solde() < 0:
            self.__solde -= chiffre
            print(f"Solde après Agios : {self.get_solde()}")

    def virement(self,destinataire,montant):
        if self.get_solde() >=0 or self.__decouvert():
            self.retrait(montant)
            destinataire.versement(montant)
            print("Virement effectuer")
        else:
            print("Solde insuffisant pour un virement")

compte1 = CompteBanquaire(24,"Rachid","Lobos", 25)
compte2 = CompteBanquaire(26,"Abdul","Puant", 0)

compte1.afficher_solde()
compte2.afficher_solde()

compte1.virement(compte2,15)

compte1.afficher_solde()
compte2.afficher_solde()
