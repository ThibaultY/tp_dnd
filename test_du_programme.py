"""
Créateur : Yohan Thibault
Groupe :407
Ce programme sert a tester le dnd_main
"""
from dnd_main import *

he = Hero("nom he", "race he", "espece he", "profession he")
kob = Kobold("nom kob", "race kob", "espece kob", "profession kob")

he.afficher_statistique()
kob.afficher_statistique()

he.attack(kob)
kob.est_en_vie()

kob.attack(he)
he.est_en_vie()

he.sac_a_dos.ajouter_item("eau", 6)
he.sac_a_dos.voir_contenu()
he.sac_a_dos.retirer_item("eau", 3)
he.sac_a_dos.ajouter_item("pioche", 1)
he.sac_a_dos.ajouter_item("bois", 1000)
he.sac_a_dos.voir_contenu()
