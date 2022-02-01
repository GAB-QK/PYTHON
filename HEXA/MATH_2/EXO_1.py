import numpy as np
from EURO_MILLION import a, b

""" Exercice
crée une liste des fréquence de chaque numéro l'indice de 0 représentera la boule 50
afficher la moyenne, l'ecart-type et la médiane """

frequences_de_a = np.zeros(50)  # création d'un Array de 50 zero pour calculer la frequence de tirage
for tirage in a:  # boucle for pour rentrer dans la premiere dimension de l'array ( les tirages )
    for boule in tirage:  # boucle for pour rentrer dans la 2em dimension de l'array ( les boules d'un tirage )
        if boule == 50:  # comme on commence indice 0 on switch le dernier 50 en index 0
            frequences_de_a[0] += 1
        else:
            frequences_de_a[boule] += 1  # ajouter 1 pour chaque réqurence de tirage
frequences_de_a = frequences_de_a / len(a)  # calculer la frequence avec la formule nombre de tirage sur somme de liste

frequences_de_b = np.zeros(12)  # identique à la methode precendente pour le tirage des étoiles
for tirage in b:
    for boule in tirage:
        if boule == 12:
            frequences_de_b[0] += 1
        else:
            frequences_de_b[boule] += 1
frequences_de_b = frequences_de_b / len(b)

for i in range(50):
    if i == 0:
        print("la frequences de la boule 50 est ", frequences_de_a[0])
    else:
        print("la frequences de la boule", i, "est ", frequences_de_a[i])
print("")

for i in range(12):
    if i == 0:
        print("la frequences de la boule 12 est ", frequences_de_b[0])
    else:
        print("la frequences de la boule", i, "est ", frequences_de_b[i])
print("")

F_A = sorted(frequences_de_a, reverse=True)     # tri des frequence dans l'ordre d"croissant
F_B = sorted(frequences_de_b, reverse=True)

for i in range(8):
    print("les boules avec les plus grandes frequences sont", np.where(frequences_de_a == F_A[i]), "de frequence ",
          F_A[i])

print("\n")

for i in range(3):
    print("les étoiles les plus tirées sont :", np.where(frequences_de_b == F_B[i]), "de frequence ", F_B[i])

""" 
Exercise
afficher  le diagramme en barres de la frequence en fonction du numéro de la boule """

"""afficher l'historamme du nombre de boules en fonction de la fréquence  ... """
