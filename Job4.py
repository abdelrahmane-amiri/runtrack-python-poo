class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}"

personne1 = Personne("Dupont", "Jean")
personne2 = Personne("Martin", "Sophie")

print(personne1.SePresenter())
print(personne2.SePresenter())
