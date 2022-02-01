import random as r

with open("liste_francais.txt", "r") as fichier:
    contenu=fichier.read().splitlines()
    print(contenu)
    fichier.seek(0) # reviens tout en haut de mon fichier txt
    Mot=fichier.readlines()
    tirage= Mot[r.randint(0,len(Mot)-1)]
    print(tirage)
