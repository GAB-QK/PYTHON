
''' Exo final : demander au user d'entrer des nombres, arreter au mot stop, puis affiche la liste des nombres entrés
ainsi que leur moyenne '''



entree= "0"
Liste=[]
while entree != "stop":
    entree= input("entre un nombre (ou stop)?")
    if entree!="stop":
        Liste.append(int(entree))
print(Liste)
print(sum(Liste)/len(Liste))




