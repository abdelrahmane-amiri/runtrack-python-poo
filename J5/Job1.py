class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"{self.name} en {self.material}"


class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "Mât": Part("Mât", "Bois"),
            "Coque": Part("Coque", "Bois"),
            "Voile": Part("Voile", "Tissu")
        }
        self.history = []

    def display_state(self):
        print(f"{self.name} :")
        for part in self.__parts.values():
            print(f"  - {part}")

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.history.append(f"Remplacement de {part_name} par {new_part}")
            self.__parts[part_name] = new_part
        else:
            print("Pièce introuvable !")

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.history.append(f"Modification du matériau de {part_name} en {new_material}")
            self.__parts[part_name].change_material(new_material)
        else:
            print("Pièce introuvable !")

    def display_history(self):
        print("Historique des modifications :")
        for change in self.history:
            print(f"  - {change}")


class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        print(f"Vitesse maximale de {self.name} : {self.max_speed} nœuds")


def menu():
    ship = Ship("Navire de Thésée")
    while True:
        print("\nMenu :")
        print("1. Afficher l'état du bateau")
        print("2. Remplacer une pièce")
        print("3. Modifier un matériau")
        print("4. Voir l'historique des modifications")
        print("5. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            ship.display_state()
        elif choix == "2":
            part_name = input("Nom de la pièce à remplacer : ")
            material = input("Matériau de la nouvelle pièce : ")
            ship.replace_part(part_name, Part(part_name, material))
        elif choix == "3":
            part_name = input("Nom de la pièce à modifier : ")
            material = input("Nouveau matériau : ")
            ship.change_part(part_name, material)
        elif choix == "4":
            ship.display_history()
        elif choix == "5":
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    menu()