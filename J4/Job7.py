import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def afficher(self):
        return f"{self.valeur} de {self.couleur}"

    def get_valeur(self):
        if self.valeur in ["Valet", "Dame", "Roi"]:
            return 10
        elif self.valeur == "As":
            return 11  
        else:
            return int(self.valeur)

class Jeu:
    def __init__(self):
        self.paquet = []
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        couleurs = ["Carreau", "Coeur", "Trèfle", "Pic"]
        
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))
        
        self.melanger_paquet()

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def piocher_carte(self):
        return self.paquet.pop() if self.paquet else None

class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.joueur_main = []
        self.croupier_main = []

    def valeur_main(self, main):
        total = sum(carte.get_valeur() for carte in main)
        nb_as = sum(1 for carte in main if carte.valeur == "As")


        while total > 21 and nb_as > 0:
            total -= 10
            nb_as -= 1
        
        return total

    def jouer(self):

        self.joueur_main = [self.jeu.piocher_carte(), self.jeu.piocher_carte()]
        self.croupier_main = [self.jeu.piocher_carte(), self.jeu.piocher_carte()]


        print("\nVotre main :", [c.afficher() for c in self.joueur_main], "Valeur:", self.valeur_main(self.joueur_main))
        print("Carte du croupier :", self.croupier_main[0].afficher())


        while self.valeur_main(self.joueur_main) < 21:
            choix = input("Voulez-vous 'prendre' une carte ou 'passer' ? (p/t) : ").lower()
            if choix == "p":
                self.joueur_main.append(self.jeu.piocher_carte())
                print("\nNouvelle main :", [c.afficher() for c in self.joueur_main], "Valeur:", self.valeur_main(self.joueur_main))
                if self.valeur_main(self.joueur_main) > 21:
                    print("Vous avez dépassé 21, vous perdez !")
                    return
            else:
                break

        
        print("\nMain du croupier :", [c.afficher() for c in self.croupier_main], "Valeur:", self.valeur_main(self.croupier_main))
        while self.valeur_main(self.croupier_main) < 17:
            self.croupier_main.append(self.jeu.piocher_carte())
            print("\nCroupier pioche :", [c.afficher() for c in self.croupier_main], "Valeur:", self.valeur_main(self.croupier_main))


        joueur_val = self.valeur_main(self.joueur_main)
        croupier_val = self.valeur_main(self.croupier_main)

        if croupier_val > 21 or joueur_val > croupier_val:
            print("Vous gagnez ! 🎉")
        elif joueur_val < croupier_val:
            print("Le croupier gagne. 😢")
        else:
            print("Égalité !")


partie = Blackjack()
partie.jouer()
