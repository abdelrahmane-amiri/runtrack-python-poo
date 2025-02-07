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
    def allerEnCourS(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai : {self.age} ans")
    
class Professeur(Personne):
    def __init__(self,matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")
        

personne = Personne()
eleve = Eleve()

eleve.afficherAge()