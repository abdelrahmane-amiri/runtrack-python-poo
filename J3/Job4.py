class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0
    
    def marquerUnBut(self):
        self.buts += 1
    
    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
    
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
    
    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
    
    def afficherStatistiques(self):
        return f"{self.nom} (n°{self.numero}, {self.position}): " \
               f"Buts: {self.buts}, Passes décisives: {self.passes_decisives}, " \
               f"Cartons jaunes: {self.cartons_jaunes}, Cartons rouges: {self.cartons_rouges}"

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []
    
    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
    
    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            print(joueur.afficherStatistiques())
    
    def mettreAJourStatistiquesJoueur(self, nom, action):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "carton_jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "carton_rouge":
                    joueur.recevoirUnCartonRouge()


if __name__ == "__main__":
 
    psg = Equipe("Paris Saint-Germain")
    marseille = Equipe("Olympique de Marseille")

    mbappe = Joueur("Kylian Mbappé", 7, "Attaquant")
    messi = Joueur("Lionel Messi", 10, "Attaquant")
    neymar = Joueur("Neymar Jr", 11, "Attaquant")

    sanson = Joueur("Valentin Rongier", 8, "Milieu")
    guendouzi = Joueur("Mattéo Guendouzi", 4, "Milieu")

    psg.ajouterJoueur(mbappe)
    psg.ajouterJoueur(messi)
    psg.ajouterJoueur(neymar)

    marseille.ajouterJoueur(sanson)
    marseille.ajouterJoueur(guendouzi)

    psg.mettreAJourStatistiquesJoueur("Kylian Mbappé", "but")
    psg.mettreAJourStatistiquesJoueur("Lionel Messi", "passe")
    marseille.mettreAJourStatistiquesJoueur("Valentin Rongier", "carton_jaune")
    psg.mettreAJourStatistiquesJoueur("Neymar Jr", "carton_rouge")

    print("Après le match :")
    psg.afficherStatistiquesJoueurs()
    marseille.afficherStatistiquesJoueurs()