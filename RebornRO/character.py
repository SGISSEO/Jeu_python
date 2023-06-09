class Character:
    def __init__(self, name, job, level):
        self.name = name
        self.job = job
        self.level = level

    def display_info(self):
        print("Name:", self.name)
        print("Job:", self.job)
        print("Level:", self.level)

def create_character():
    name = input("Enter character name: ")
    job = input("Enter character job: ")
    level = int(input("Enter character level: "))

    character = Character(name, job, level)
    return character

# Créer un personnage
new_character = create_character()

# Afficher les informations du personnage
new_character.display_info()
