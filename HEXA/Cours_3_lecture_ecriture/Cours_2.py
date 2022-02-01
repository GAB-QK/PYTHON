import random as r
'''Exo
lire  le fichier liste_francais.txt ete créer une liste  de  tous les mots contenus dans ce fichier'''

with open("liste_francais.txt", "r") as fichier:
    contenu=fichier.read().splitlines()
    Liste =contenu
    print(Liste)
    fichier.seek(0) #remet tout en haut dans mon fichier txt
    Mot=fichier.readlines()
    print(Mot[r.randint(0,len(Mot)-1)])




