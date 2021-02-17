"""
Créateur : Yohan Thibault
Groupe :470
Ce programme fait la création de personnages de personnage de jeu de dnd
"""
from roll_dice import *
from dataclasses import dataclass
from enum import Enum


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

    @staticmethod
    def attack(target):
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
        self.sac_a_dos = SacADos()


class Alignement(Enum):
    LOYAL_BON = 0
    NEUTRE_BON = 1
    CHAOTIQUE_BON = 2
    LOYAL_NEUTRE = 3
    NEUTRE_NEUTRE = 4
    CHAOTIQUE_NEUTRE = 5
    LOYAL_MAUVAIS = 6
    NEUTRE_MAUVAIS = 7
    CHAOTIQUE_MAUVAIS = 8
    NONE = 9


@dataclass
class Item:
    nom_item: str
    quantite: int


class SacADos:
    def __init__(self):
        self.liste_item = []

    def voir_contenu(self):
        print("----------------")
        print("INVENTAIRE :")
        print("#N\tItem\tQunatiée")
        for item in range(len(self.liste_item)):
            print(f"{item}\t{self.liste_item[item].nom_item} :\t{self.liste_item[item].quantite}")
        print("----------------")

    def is_item_there(self, serched_item):
        is_item_there = False
        emplacement = int
        for i in range(len(self.liste_item)):
            if serched_item in self.liste_item[i].nom_item:
                is_item_there = True
                emplacement = i
        return is_item_there, emplacement

    def ajouter_item(self, nom_item, quantite):
        item = Item(nom_item, quantite)
        is_item_there, emplacement = self.is_item_there(item.nom_item)

        if is_item_there:
            self.liste_item[emplacement].quantite += item.quantite
            print(f"Il y a {item.quantite} qui vont être ajouté aux {item.nom_item}")

        else:
            print(f"Il n'y avait pas de {item.nom_item}")
            print("Alors l'item sera ajouté")
            self.liste_item.append(item)
        #  self.voir_contenu()

    def retirer_item(self, nom_item, quantite):
        """
        Remove items in the backpack.
        :return: ?
        """
        item = Item(nom_item, quantite)
        is_item_there, emplacement = self.is_item_there(item.nom_item)

        if is_item_there:
            if item.quantite <= self.liste_item[emplacement].quantite:
                self.liste_item[emplacement].quantite -= item.quantite
                if self.liste_item[emplacement].quantite > 0:
                    print(f"Il y a {item.quantite} de {item.nom_item} qui vont être soustrait")
                else:
                    print(f"Il n' y a plus de {item.nom_item}.")
                    print("L'espace va donc être libérée.")
                    self.liste_item.pop(emplacement)
            else:
                print(f"ERREUR le nombre de {item.nom_item} est trop grand")
        else:
            print(f"Il n'y a pas de {item.nom_item} dans votre sac")
            print(f"ERREUR")
        #  self.voir_contenu()
