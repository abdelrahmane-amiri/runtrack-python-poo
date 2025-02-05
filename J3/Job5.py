import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
        self.vie_max = vie
    
    def attaquer(self, adversaire):
        """Attaque l'adversaire avec des dégâts aléatoires"""
        degats = random.randint(10, 20)
        adversaire.vie = max(0, adversaire.vie - degats)
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts !")
    
    def estVivant(self):
        """Vérifie si le personnage est encore en vie"""
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None
    
    def choisirNiveau(self):
        """Demande et définit le niveau de difficulté"""
        while True:
            try:
                self.niveau = int(input("Choisissez un niveau de difficulté (1-3) : "))
                if 1 <= self.niveau <= 3:
                    break
                else:
                    print("Veuillez choisir un niveau entre 1 et 3.")
            except ValueError:
                print("Entrée invalide. Entrez un nombre entre 1 et 3.")
    
    def lancerJeu(self):
        """Lance le jeu avec les paramètres du niveau choisi"""
        if not self.niveau:
            self.choisirNiveau()
        
        
        vie_joueur = 100 * self.niveau
        vie_ennemi = 80 * self.niveau
        
        self.joueur = Personnage("Héros", vie_joueur)
        self.ennemi = Personnage("Monstre", vie_ennemi)
        
        self.combattre()
    
    def combattre(self):
        """Gère le déroulement du combat"""
        print(f"Début du combat ! {self.joueur.nom} vs {self.ennemi.nom}")
        print(f"{self.joueur.nom}: {self.joueur.vie} PV | {self.ennemi.nom}: {self.ennemi.vie} PV")
        
        while self.joueur.estVivant() and self.ennemi.estVivant():
           
            input("Appuyez sur Entrée pour attaquer...")
            self.joueur.attaquer(self.ennemi)
            print(f"{self.ennemi.nom}: {self.ennemi.vie} PV restants")
            
        
            if not self.ennemi.estVivant():
                self.verifierVictoire()
                break
            
            self.ennemi.attaquer(self.joueur)
            print(f"{self.joueur.nom}: {self.joueur.vie} PV restants")
            
            if not self.joueur.estVivant():
                self.verifierVictoire()
                break
    
    def verifierVictoire(self):
        """Vérifie et annonce le vainqueur"""
        if self.joueur.estVivant():
            print(f"\n🏆 {self.joueur.nom} a remporté le combat !")
        else:
            print(f"\n☠️ {self.ennemi.nom} a vaincu {self.joueur.nom} !")

if __name__ == "__main__":
    jeu = Jeu()
    jeu.lancerJeu()