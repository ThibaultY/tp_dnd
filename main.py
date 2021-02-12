"""
Créateur : Yohan Thibault
Groupe :470
Ce programme fait la création de personnages de personnage de jeu de dnd
"""
from roll_dice import *


class NPC:
    def __init__(self, nom, race, espece, profession):
        self.profession = profession
        self.espece = espece
        self.race = race
        self.nom = nom

        self.classe_armure = RollDice("1D12").sum()
        self.point_de_vie = 20  # RollDice("1D20").sum()

        self.force = RollDice("4D6").keep_max(3)
        self.agilite = RollDice("4D6").keep_max(3)
        self.constitution = RollDice("4D6").keep_max(3)
        self.intelligence = RollDice("4D6").keep_max(3)
        self.sagesse = RollDice("4D6").keep_max(3)
        self.charisme = RollDice("4D6").keep_max(3)

    def afficher_statistique(self):
        print(',\n'.join("%s: %s" % item for item in vars(self).items()))

    def attack(self, target):
        attack = RollDice("1D20").sum()
        if attack == 20:  # attaque critique
            print("attaque critique.")
            target.subir_dommage(RollDice("1D8").sum())
        elif attack == 1:
            print("attaque ratée.")
        else:
            if attack >= target.classe_armure:
                target.subir_dommage(RollDice("1D6").sum())

    def subir_dommage(self, dommage):
        print(f"Votre personnage est passé de {self.point_de_vie}")
        self.point_de_vie -= dommage
        print(f"Votre personnage est passé de {self.point_de_vie}")


# n = NPC("Yohan", "humanoide", "humain", "Constructeur")

# n.afficher_statistique()


class Kobold(NPC):
    def __init__(self, nom, race, espece, profession):
        super().__init__(nom, race, espece, profession)


# o = Kobold("Xavier", "humanoide", "humain", "Constructeur")
# o.attack(n)

class Hero(NPC):
    def __init__(self, nom, race, espece, profession):
        super().__init__(nom, race, espece, profession)


cob = Kobold("Xavier", "humanoide", "humain", "Constructeur")
he = Hero("Yohan", "something", "espece", "fermier")

print(f"cible à maintenant {cob.point_de_vie}")
print(f"cible à maintenant {he.point_de_vie}")
he.attack(cob)