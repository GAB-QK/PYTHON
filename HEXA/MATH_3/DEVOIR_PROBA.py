""""""
import math as math
import random as r
import numpy as np
"""
EXO_1
ecrire une fonction qui prend en parametre p, n et k et qui renvoie la proba
de p(k) d'après la loi binomial
"""
import scipy.special as sp

def probabilite_1(p, n, k):
    resultat = (sp.comb(n, k)) * p ** (k) * (1 - p) ** (n - k)
    return resultat


print(probabilite_1(0.3, 10, 3))

"""
EX0_2
Ecrire une fonction qui prend en parametre p,n et k et qui renvoie 
la probabilité P(x>=k) d'avoir au moins k succès sur n partie 
"""


def probabilite_2(p, n, k):
    P_X = 0
    for i in range(k):
        P_X += probabilite_1(p, n, i)  # P(x>=K) = 1 - somme de P(X=0) à P(X=K)
    resultat = 1 - P_X
    return resultat


print(probabilite_2(0.3, 20, 4))

"""
EXO_3
Ecrire une fonction qui prends parametres p,n et qui simule n parties 
avec le module random et renvoie une liste de n booléens ( TRUE pour 
un succès et FALSE pour un echec 
"""
def probabilite_3(p, n):
    liste_booleen = []
    for i in range(n):
        tirage = r.random()
        if tirage < p:
            liste_booleen.append(True)
        else:
            liste_booleen.append(False)
    return liste_booleen

probabilite_3(1/2, 10)

"""
EXO_4
Ecrire une fonction qui prend en parametre p,n et N le nombre d'éxperience
et qui simule N fois l'experience précédente et qui renvoie une liste
de taille n+1 où l'élément i correspond à la frequence des parties ou il
y a eu i succès 
"""

def probabilite_4(p, n, N):
    liste = np.zeros(n+1)
    for i in range(N):
        liste_booleen = probabilite_3(p, n)
        succes = liste_booleen.count(True)
        liste[succes] += 1
    for i in range(len(liste)):
        liste[i] = liste[i]/N            # comme c'ets un array on peut ton simplement faire "return liste/N
    return liste



print("P-4", probabilite_4(1/2, 5, 10))


import matplotlib.pyplot as plt
p = 0.3
N = 1000
n = 10
x = np.arange(n+1)
y = probabilite_4(p, n, N)
plt.bar(x, y)

y2 = probabilite_1(p, n, x)
plt.plot(x, y2, "r+-")

plt.xlabel("succes")
plt.ylabel("frequences")
plt.show()
