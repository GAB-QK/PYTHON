""" fonction qui calcule le nombre de boules en fonction de leur frequence
elle prend en parametre une liste de frequence et une rpecision
et elle renvoie la liste des abscisses et des ordonnées"""
from EXO_1 import *

frequence = liste/nb_tirage

def histogramme_freq(frequence, n):
    x = np.linspace(0, 1, n)        # crée un arrey de même taille que l'arrey qu'on lui donne
    y = np.zeros_like(x)            # mais remploe de zeros
    for f in frequence:             # int(f*n) +=1 donne l'indice dans la liste y
        y[int(f * n)] += 1          # ou tombe la frequence f é"'(§è!ç
    return x, y


plt.figure()
x, y = histogramme_freq(liste / nb_tirage, 100)
plt.plot(x, y)
plt.show()


"""
quelque stat sur les fréquence 
"""


print("moyenne",np.mean(frequence)) # methode maen de np calcul la moyenne
print("ecart-type",np.std(frequence))    # methode std de np calcul ecart type
print("mediane",np.median(frequence))   # methode median de np pour calculer la mediane statistique