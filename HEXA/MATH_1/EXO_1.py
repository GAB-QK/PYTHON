import random
import random as r
import matplotlib.pyplot as plt
import numpy as np


def EURO(n, k):
    liste = []
    for i in range(n):
        A = r.randint(1, k)
        if A not in liste:
            liste.append(A)
            liste.sort()

    return liste


print("ici",EURO(5,50))

def Euro_2(n, k):
    boules = [i for i in range(n)]      # comprehension de liste
    return r.sample(boules, k)          # equivaut à liste =
                                        # for i in range (n)
                                        # liste.append(f(i))

# print(Euro_2(10,2))

def Million(n, k, nb):
    liste_2 = np.zeros(n)
    for i in range(nb):
        t = Euro_2(n, k)
        for boule in t:
            liste_2[boule] += 1
    return liste_2

nb_tirage = 100
liste = Million(50, 5, 50)
print(liste)
print(sum(liste))

"""Exercice 
afficher l'histogramme des fréquence d'apparitiokn de chaques boules """

boules = [i for i in range(len(liste))]
plt.bar(boules, liste / 50)
plt.xlabel("numéro")
plt.ylabel("fréquence")

plt.show()


""" equivalent de la fonction random.sample
tire au hasard k element parmi la liste sans remise"""
def tirage_3(liste,k):
    copie=liste.copy()  # crée une copie de la liste
    resultat=[]
    for i in range (k):
        indice = random.randint(0,len(copie)-1)
        # on elnève cette éléments de la copie
        # et on l'ajoute au resultat
        resultat.append(copie.pop(indice))      # pop va enlever la valeur d'indice indiqué
                                                # de ma liste et renvoie cette valeur
    return resultat

print(tirage_3(["a","b","c","d"],2))