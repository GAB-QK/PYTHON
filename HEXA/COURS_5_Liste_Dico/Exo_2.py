from TRI_Aure import *

#  calcul la diff de temps et ajout dans une liste avec la liste tailles quiprend ici le parametre "n"
# le parametre "a" ici prend le nom de la fonction de Tri
for i in tailles:
    sort.append(tri("sort", i))
print("sort:", sort)
for i in tailles:
    selection.append(tri("selection", i))
print("selection", selection)
for i in tailles:
    insertion.append(tri("insertion", i))
print("insertion", insertion)


