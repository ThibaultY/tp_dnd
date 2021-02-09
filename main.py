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


n = NPC("Yohan", "humanoide", "humain", "Constructeur")

n.afficher_statistique()


class Kobold(NPC):
    def __init__(self, nom, race, espece, profession):
        super().__init__(nom, race, espece, profession)

    def attack(self, cible):
        attack = 20  # RollDice("1D20")

        if attack == 20:  # attaque critique
            print("attaque critique.")
            direct_attack = RollDice("1D8")
            cible.point_de_vie -= direct_attack
            print(f"cible à maintenant {cible.point_de_vie}")
        elif attack == 1:
            print("attaque ratée.")
        else:
            pass

    def subir_dommage(self, dommage):
        pass


o = Kobold("Xavier", "humanoide", "humain", "Constructeur")


o.attack(n)

class Hero(NPC):
    def __init__(self):
        super().__init__()