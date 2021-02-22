"""
Créateur : Yohan Thibault
Groupe :407
Ce programme est un jeu dnd sous usilisant la console python
"""
from roll_dice import *
from dataclasses import dataclass
from enum import Enum


class NPC:
    def __init__(self, nom, race, espece, profession):
        self.profession = profession
        self.espece = espece
        self.race = race
        self.nom = nom
        self.alignement = Alignement.NONE

        self.classe_armure = RollDice("1D12").sum()
        self.point_de_vie = RollDice("1D20").sum()

        self.force = RollDice("4D6").keep_max(3)
        self.agilite = RollDice("4D6").keep_max(3)
        self.constitution = RollDice("4D6").keep_max(3)
        self.intelligence = RollDice("4D6").keep_max(3)
        self.sagesse = RollDice("4D6").keep_max(3)
        self.charisme = RollDice("4D6").keep_max(3)

    def afficher_statistique(self):
        print("----------------")
        print(',\n'.join("%s: %s" % item for item in vars(self).items()))
        print("----------------")

    @staticmethod
    def attack(target):
        """
        Generates the amount of damage that the target is going to take.
        :param target: object target
        """
        print("----------------")
        attack = RollDice("1D20").sum()
        print(f"Le dé 20 donne : {attack}")
        if attack == 20:
            print("Attaque critique.")
            target.subir_dommage(RollDice("1D8").sum())
        elif attack == 1:
            print("Attaque royalement ratée.")
        else:
            print("Attaque normale, ", end="")
            if attack >= target.classe_armure:
                print("réussi.")
                target.subir_dommage(RollDice("1D6").sum())
            else:
                print("ratée.")

    def subir_dommage(self, dommage):
        """
        Makes the character loose health.
        :param dommage: amount of damage taken (int)
        """
        print(f"{self.nom} avait {self.point_de_vie} point de vie,")
        print(f"À reçu {dommage} de dommage")
        self.point_de_vie -= dommage
        print(f"{self.nom} personnage à maintenant : {self.point_de_vie}")

    def est_en_vie(self):
        """
        Check if the character is alive:
        :return: bool (True : character is alive, False: character is dead)
        """
        if self.point_de_vie <= 0:
            print(f"{self.nom} est mort! Oh non!")
            return False
        else:
            print(f"{self.nom} tient toujours debout!")
            return True


class Kobold(NPC):
    def __init__(self, nom, race, espece, profession):
        super().__init__(nom, race, espece, profession)


class Hero(NPC):
    def __init__(self, nom, race, espece, profession):
        super().__init__(nom, race, espece, profession)
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
        """
        To see what is in the sac in a fancy way
        """
        print("----------------")
        haut_du_tableau = "¦  #N  ¦   Item   ¦ Qunatiée ¦"  # Will help with calculation
        print("INVENTAIRE :")
        print('\033[7m' + haut_du_tableau + '\033[0m')
        for item in range(len(self.liste_item)):
            # the information of the table (it's all one line)
            print("¦ ", item, " " * (3-len(str(item))) + "¦",  # Item placement in the inventory
                  self.liste_item[item].nom_item, " " * (8 - len(self.liste_item[item].nom_item)) + "¦",  # Item name
                  self.liste_item[item].quantite, " " * (8 - len(str(self.liste_item[item].quantite))) + "¦")  # Item quantity

        print("¯" * len(haut_du_tableau))  # The buttom line of the table
        print("----------------")

    def is_item_there(self, serched_item):
        """
        check if an item is already in the sac
        :param serched_item: Name of the item
        :return:
                - Bool (if the item is there or not),
                - The index of the item in the list.
        """
        is_item_there = False
        emplacement = int
        for i in range(len(self.liste_item)):
            if serched_item in self.liste_item[i].nom_item:
                is_item_there = True
                emplacement = i
        return is_item_there, emplacement

    def ajouter_item(self, nom_item, quantite):
        """
            Adds items in the backpack.
            :param nom_item: Name of the item (be careful on the spelling)
            :param quantite: quantity of item
        """
        item = Item(nom_item, quantite)
        is_item_there, emplacement = self.is_item_there(item.nom_item)

        if is_item_there:
            self.liste_item[emplacement].quantite += item.quantite
            print(f"Il y a {item.quantite} qui vont être ajouté aux {item.nom_item}.")

        else:
            print(f"Il n'y avait pas de {item.nom_item}.")
            print(f"Alors l'item sera ajouté {item.quantite} de fois.")
            self.liste_item.append(item)

    def retirer_item(self, nom_item, quantite):
        """
        Remove items in the backpack.
        :param nom_item: Name of the item (be careful on the spelling)
        :param quantite: quantity of item
        """
        item = Item(nom_item, quantite)
        is_item_there, emplacement = self.is_item_there(item.nom_item)

        if is_item_there:

            if item.quantite <= self.liste_item[emplacement].quantite:  # if the amount remove is to big
                self.liste_item[emplacement].quantite -= item.quantite
                if self.liste_item[emplacement].quantite > 0:  # Check if there is no more of the item.
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
