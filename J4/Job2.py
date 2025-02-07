class Personne:
    def __init__(self,age = 14):
        self.age = age
    
    def afficherAge(self):
        print(f"J'ai : {self.age} ans")
        
    def bonjour(self):
        print('Hello')

    def ModifierAge(self,age):
        self.age = age



class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai : {self.age} ans")
    
class Professeur(Personne):
    def __init__(self,age,matiereEnseignee):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")
        

personne = Personne()
eleve = Eleve()
professeur = Professeur(40,"Mathematique")

eleve.bonjour()
eleve.allerEnCours()
eleve.ModifierAge(15)
eleve.afficherAge()

professeur.bonjour()
professeur.enseigner()
professeur.afficherAge()