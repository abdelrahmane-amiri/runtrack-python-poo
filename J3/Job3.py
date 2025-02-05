class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"
    
    def __str__(self):
        return f"Tâche: {self.titre} - {self.description} (Statut: {self.statut})"

class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache):
        """Ajoute une tâche à la liste"""
        self.taches.append(tache)
    
    def supprimerTache(self, titre):
        """Supprime une tâche par son titre"""
        self.taches = [tache for tache in self.taches if tache.titre != titre]
    
    def marquerCommeFinie(self, titre):
        """Marque une tâche comme terminée"""
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminé"
                break
    
    def afficherListe(self):
        """Retourne la liste de toutes les tâches"""
        return self.taches
    
    def filterListe(self, statut):
        """Filtre les tâches par statut"""
        return [tache for tache in self.taches if tache.statut == statut]

if __name__ == "__main__":
    ma_liste = ListeDeTaches()

    tache1 = Tache("Courses", "Acheter du pain et du lait")
    tache2 = Tache("Ménage", "Passer l'aspirateur")
    tache3 = Tache("Travail", "Terminer le rapport")

    ma_liste.ajouterTache(tache1)
    ma_liste.ajouterTache(tache2)
    ma_liste.ajouterTache(tache3)

    print("Toutes les tâches :")
    for tache in ma_liste.afficherListe():
        print(tache)

    ma_liste.marquerCommeFinie("Courses")

    ma_liste.supprimerTache("Ménage")

    print("\nTâches à faire :")
    for tache in ma_liste.filterListe("à faire"):
        print(tache)