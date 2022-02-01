import random
import time
# init des  variable et liste vide nécéssaire
insertion = []
selection = []
sort = []
tailles = [100, 200, 500, 1000, 2000, 5000, 10000, 20000]

# def de la fonction liste qui  crée une liste random de longueur "n"
def liste(n):
    liste = [random.random() for i in range(n)]
    return liste

# def de la fonction swap
def swap(liste, i, j):
    aux = liste[i]
    liste[i] = liste[j]
    liste[j] = aux

# def des diférentes fonction de tri
def tri_insertion(liste):
    for i in range(1, len(liste)):
        j = i - 1
        while j >= 0 and liste[j + 1] < liste[j]:
            swap(liste, j, j + 1)
            j -= 1


def tri_selection(liste):
    for i in range(0, len(liste)):
        m = liste[i:].index(min(liste[i:]))
        swap(liste, i, m+i)


def tri_sort(liste):
    liste.sort()

# fonctions qui fait la dif de temps de calcul des dif fonction de tri
def tri(a, n):
    methode = None
    if a == "insertion":
        methode = tri_insertion

    elif a == "selection":
        methode = tri_selection

    elif a == "sort":
        methode = tri_sort

    t1 = time.time()
    methode(liste(n))
    t2 = time.time()
    return t2 - t1      # calcul de la dif de temps en dehors des if/elif/else
