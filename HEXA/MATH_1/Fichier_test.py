print('G','F','G', sep='-')

import random as r

liste = [r.randint(1,10) for i in range(20)]
print(liste)


for elt in liste :
    print(elt)

for i, elt in enumerate(liste):
    print(f"a l'indice {i} se trouve {elt}.")

for elt in enumerate(liste):
    print(elt)

def decomposer (entier, divis_par):
    p_e = entier // divis_par
    reste = entier % divis_par
    return p_e, reste

gab , morgane = decomposer(20,3)
print(gab,morgane)
help(print)
