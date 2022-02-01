'''Exercice
créer un dico de 4 élémentsqui associe à un nom d'élèce une note
demander au user dee rentrer 4 motset 4 notes puis afficher le dico et la moyenne de la classe '''

nb_eleve=int(input("nombre d'élève ?"))
Dico={"moyenne":0}

for i in range(nb_eleve):
    nom = input("nom de l'élève")
    note = int(input("donne ta note zeuuuubi !"))
    Dico[nom] = note
    Dico["moyenne"] += note
Dico["moyenne"] = Dico["moyenne"]/nb_eleve
print(Dico)








