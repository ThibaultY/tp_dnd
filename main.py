"""
Créateur : Yohan Thibault
Groupe :470
Ce programme fait la création de personnages de personnage de jeu de dnd
"""
from roll_dice import *


class NPC:
    def __init__(self, nom, race, espece, profession):
        self.profession = profession
        self.point_de_vie = RollDice("1D20").sum()
        self.espece = espece
        self.race = race
        self.classe_armure = RollDice("1D12").sum()
        self.force = RollDice("4D6").keep_max(4)
        self.agilite = RollDice("4D6").keep_max(4)
        self.constitution = RollDice("4D6").keep_max(4)
        self.intelligence = RollDice("4D6").keep_max(4)
        self.sagesse = RollDice("4D6").keep_max(4)
        self.charisme = RollDice("4D6").keep_max(4)

    def afficher_statistique(self):
        print(',\n'.join("%s: %s" % item for item in vars(self).items()))


n = NPC("humanoide", "humain", 40, "Constructeur")

n.afficher_statistique()


class Kobold(NPC):
    def __init__(self):
        super().__init__()

    def attack(self, hero):
        pass

    def subir_dommage(self, dommage):
        pass


class Hero:
    def __init__(self):
        pass