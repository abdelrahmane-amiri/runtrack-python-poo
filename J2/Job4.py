class Student:
    def __init__(self,nom,prenom,id):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = 0
        self.__level = self.__student_eval()

    def student_info(self):
        return f"Nom : {self.__nom} \nPrenom : {self.__prenom} \nId : {self.__id} \nNiveau : {self.__level}"


    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")

    def get_credits(self):
        return self.__credits
    
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def get_eval(self):
        return self.__student_eval()
            
    

etudiant = Student("John", "Doe", 145)

print(etudiant.student_info())
etudiant.add_credits(10)
etudiant.add_credits(20)
etudiant.add_credits(50)

print(f"Total des crédits : {etudiant.get_credits()}")
