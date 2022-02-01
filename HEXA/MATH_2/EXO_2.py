from EXO_1 import *

G_C = [5, 21, 12, 38, 9, 16, 19]  # on recupère manuelement la liste récuperer des plus grande frquence
freqfreq = 0                        # d'apparition de boules
n = 0
reccurence = {}

for tirage in a:                                            # dans a on prend un tirage
    for boule in tirage:                                    # on pracoure les boules de ce même tirage
        if boule == G_C[n]:                                 # si la boule = boule d'indice indiqué par n
            for boule_2 in tirage:                          # et si après appariton de boule etant dans G_C
                if boule_2 != boule and boule_2 in G_C:
                    for boule_3 in tirage:
                        if boule_3 != boule and boule_3 != boule_2 and boule_3 in G_C:
                            reccurence[boule_2] = boule_3        # on ajoute a liste la recurence
                            freqfreq += 1
                                                                # excepté cette même boule alors
                                                                # et on ajoute a freqfreq +1 pour calculer la proba
freqfreq = freqfreq / len(a)                                    # calcul de proba avec freqfreq

print(f"\n la frequence que la boule {G_C[n]} tombe avec \n"
      f"deux boule de la liste {G_C} est de ", freqfreq)
print("\n liste des occurences : ")
print(reccurence)