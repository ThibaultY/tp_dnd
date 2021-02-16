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


@dataclass
class Item:
    nom_item: str
    quantite: int


class SacADos:
    def __init__(self):
        self.liste_item = []

    def is_item_there(self, serched_item):
        is_item_there = False
        emplacement = int
        for i in range(len(self.liste_item)):
            if serched_item in self.liste_item[i]:
                is_item_there = True
                emplacement = i
        return is_item_there, emplacement

    def retirer_item(self, item):
        """
        Add items in the backpack.
        :param item: Item class
        :return: ?
        """
        sub_item = [item.nom_item, item.quantite]
        is_item_there, emplacement = self.is_item_there(sub_item[0])

        if is_item_there:
            if sub_item[1] <= self.liste_item[emplacement][1]:
                self.liste_item[emplacement][1] = self.liste_item[emplacement][1] - sub_item[1]
                if self.liste_item[emplacement][1] > 0:
                    print(f"Il y a {sub_item[1]} de {sub_item[0]} qui vont être soustrait")
                else:
                    print(f"Il n' y a plus de {sub_item[0]}.")
                    print("L'espace va donc être libérée.")
                    self.liste_item.pop(emplacement)
            else:
                print(f"ERREUR le nombre de {sub_item[0]} est trop grand")
        else:
            print(f"Il n'y a pas de {sub_item[0]} dans votre sac")
            print(f"ERREUR")

        print("Votre sac à dos : ", ', '.join(map(str, self.liste_item)))

    def ajouter_item(self, item):
        add_item = [item.nom_item, item.quantite]
        is_item_there, emplacement = self.is_item_there(add_item[0])

        if is_item_there:
            self.liste_item[emplacement][1] = add_item[1] + self.liste_item[emplacement][1]
            print(f"Il y a {add_item[1]} qui vont être ajouté aux {add_item[0]}")
            print("Votre sac à dos : ", ', '.join(map(str, self.liste_item)))

        else:
            print(f"Il n'y avait pas de {add_item[0]}")
            print("Alors l'item sera ajouté")
            self.liste_item.append(add_item)
        print("Votre sac à dos : ", ', '.join(map(str, self.liste_item)))


eau2 = Item("eau", 2)
eau1 = Item("eau", 4)
eau24 = Item("eau", 24)
eau14 = Item("eau", 14)
cobol32 = Item("Cobol Stone", 32)
random29 = Item("random", 1)
sac = SacADos()
list_test = [["you", 2], ["yt", 1], ["youTube", 3], ["yet",  4]]

print(eau2)
sac.ajouter_item(eau2)
sac.ajouter_item(eau2)
sac.ajouter_item(eau2)
sac.ajouter_item(eau2)
sac.ajouter_item(eau2)
sac.ajouter_item(eau1)
sac.ajouter_item(cobol32)
sac.ajouter_item(cobol32)
sac.ajouter_item(cobol32)
sac.ajouter_item(cobol32)
sac.retirer_item(cobol32)
sac.retirer_item(eau24)
sac.retirer_item(random29)
sac.retirer_item(eau14)
