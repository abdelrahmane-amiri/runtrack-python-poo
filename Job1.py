class Operation:
    def __init__(self, nombre1=12, nombre2=5):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def afficher(self):
        print(f"Nombre 1: {self.nombre1}\nNombre 2: {self.nombre2}")

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Resultat: {resultat}")

operation = Operation()

print(operation)

operation.afficher()

operation.addition()