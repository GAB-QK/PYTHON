''' Exo
écrire un programme qui print "pile" ou "face" de maniere random
avec une chance  sur deux pour chaque possibilité'''

import random as R

Tirage= R.randint(1,2)
if Tirage == 1:
    print("Pile")
else:
    print("Face")


# tirer au  hasard un element  d'une liste

print(R.choice(["A","B","C","D"]))

# exemple pile face

print(R.choice(["pile","face"]))

# tirage au  hasard avec  un float entre 0 et 1

print(R.random())

#Exemple : pile ou face

if R.random()<0.5:
    print("Pile")
else:
    print("Face")

# on peut choisir precisement la possibilité et la proba


import math as M

print(M.sqrt(49))
print(M.exp(1))
print(M.pi)

