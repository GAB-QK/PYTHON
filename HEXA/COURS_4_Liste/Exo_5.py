''' exercice
1)demander d'entrer des nombres
ce que l'utilisateur entre le mot "stop"
2) afficher la somme des nombres entrés
'''


entree = "0"
Somme = 0
while entree != "stop":
    Somme = Somme + int(entree)
    entree= input("entre un nombre (ou stop)")
print(Somme)













