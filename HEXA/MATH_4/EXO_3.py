""" on va représenter un graphe par un dico don les clés
sont les noeuds du graphe et les valeurs sont les listes 
des noeuds vers lesquels il ya un une arêtes """
import numpy as np

graphe = {}
# on ajoute les noeuds
for noeud in "ABCDE":
    graphe[noeud] = []
# on ajoute lmes arêtes
graphe["A"] += ["B", "D"]
graphe["B"] += ["B", "C"]
graphe["C"] += ["A", "B", "D"]
graphe["D"] += ["A", "E"]
graphe["E"] += ["C", "E"]

'''
Exercice 
Ecrire une fonction qui prend en parametre un graphe et 2 noeuds a et b 
et qui ajoute au graphe une arrête de a vers b
'''


def matrice(G: dict, a, b):
    if a not in G:
        G[a] = []
    if b not in G:
        G[b] = []
    if b not in G:
        G[a] += [b]
    return G


matrice(graphe, "A", "C")
matrice(graphe, "E", "F")
print(matrice)
'''
Exercice 
Ecrire une fonction qui prend en parametre un graphe et qui renvoie 
sa matrice d'adjacence 
'''

def adjacence(G):
    matrice_vide = np.zeros((len(G),  len(G)), dtype=int)
    # pn parcours les nopeuds du graphe avec n1
    # et les lignes de la matrice avec j
    i = 0
    for n1 in G:
        # pour chaque ligne i et noeud n1
        # on parcourt les noeuds du graphe avec n2
        # et les colonnes de la matrice j
        j = 0
        for n2 in G:
            # si il y une arête de n1 vers n2
            # pn passe l'élément i,j de la matrice à 1
            if n2 in G[n1]:
                matrice_vide[i, j] = 1
            j += 1  # colonne suivante
        i += 1   # ligne suivante
    return matrice_vide
    
print(adjacence(graphe))


''' 
Exercice 
Ecrire une fonctiokn qui prend en parametre un graphe et une liste de noeuds et qui
teste si la liste correspond à un chemin valide sur le graphe ( renvoie un booléen )
 '''

def valide(G,chemiin):
    for i in range(len(chemiin-1)):
        # on teste si le noeud est dans le graphe
        if chemiin[i] not in G:
            return False
        # on teste s'il y a une arête entre ce noeud et le suivant
        if chemiin[i+1] not in G[chemiin[i]]:
            return False
    return True
