"""
Créateur : Yohan Thibault
Groupe :470
Ce programme fait la création de personnages de personnage de jeu de dnd
"""
from roll_dice import *
from dataclasses import dataclass


class NPC:
    def __init__(self, nom, race, espece, profession, alignement):
        self.profession = profession
        self.espece = espece
        self.race = race
        self.nom = nom
        self.alignement = alignement

        self.classe_armure = RollDice("1D12").sum()
        self.point_de_vie = RollDice("1D20").sum()

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
        print(f"Le dé 20 donne : {attack}")
        if attack == 20:
            print("attaque critique.")
            target.subir_dommage(RollDice("1D8").sum())
        elif attack == 1:
            print("attaque royalement ratée.")
        else:
            print("Attaque normale, ", end="")
            if attack >= target.classe_armure:
                print("réussi.")
                target.subir_dommage(RollDice("1D6").sum())
            else:
                print("ratée.")

    def subir_dommage(self, dommage):
        print(f"{self.nom} avait {self.point_de_vie} point de vie,")
        print(f"À reçu {dommage} de dommage")
        self.point_de_vie -= dommage
        print(f"{self.nom} personnage à maintenant : {self.point_de_vie}")

    @property
    def est_en_vie(self):
        if self.point_de_vie < 0:
            return False
        else:
            return True


class Kobold(NPC):
    def __init__(self, nom, race, espece, profession, alignement):
        super().__init__(nom, race, espece, profession, alignement)


class Hero(NPC):
    def __init__(self, nom, race, espece, profession, alignement):
        super().__init__(nom, race, espece, profession, alignement)


@dataclass
class Item:
    quantite: int
    nom_item: str

class SacADos:
    def __init__(self, liste_item):
        self.liste_item = liste_item


he = Hero("hero", "humain", "thing", "jojo fan", "LB")
