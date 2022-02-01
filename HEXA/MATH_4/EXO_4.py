'''
On va représenter un graphe non orienté pondéré, c'est à dire
un graphe dans lequel les arêtes ont une longueur
On va utiliser un dictionnaire de dictionnaires
'''


def ajouter_arete(graphe, n1, n2, longueur):
    if n1 not in graphe:
        graphe[n1] = {}
    if n2 not in graphe:
        graphe[n2] = {}
    graphe[n1][n2] = longueur
    graphe[n2][n1] = longueur


carte = {}
ajouter_arete(carte, "Paris", "Lyon", 393)
ajouter_arete(carte, "Paris", "Lille", 225)
ajouter_arete(carte, "Paris", "Strasbourg", 495)
ajouter_arete(carte, "Paris", "Orléans", 132)
ajouter_arete(carte, "Paris", "Le Havre", 197)
ajouter_arete(carte, "Lyon", "Marseille", 314)
ajouter_arete(carte, "Lyon", "Grenoble", 111)
ajouter_arete(carte, "Orléans", "Nantes", 335)
ajouter_arete(carte, "Orléans", "Rennes", 307)
ajouter_arete(carte, "Nantes", "Rennes", 113)
ajouter_arete(carte, "Nantes", "Bordeaux", 346)
ajouter_arete(carte, "Bordeaux", "Toulouse", 244)
ajouter_arete(carte, "Lyon", "Toulouse", 537)
ajouter_arete(carte, "Rennes", "Brest", 242)
# print(carte)

'''
carte[n1] est le dictionnaire qui représente
les arêtes du noeud 1
carte[n1][n2] est la distance associée à l'arête n1-n2
'''

'''
L'algorithme de Dijkstra permet de trouver le plus court chemin
entre deux noeuds
'''


def dijkstra(graphe, depart, arrivee):
    villes_vues = [depart]
    villes_a_voir = [v for v in graphe[depart]]
    # on initialise les scores du départ et de ses
    # villes adjacentes
    score = {depart: 0}
    for v in villes_a_voir:
        score[v] = graphe[depart][v]

    # Pour chaque ville vue, on garde en mémoire
    # la ville précédente le long du plus court chemin
    precedente = {}
    for v in villes_a_voir:
        precedente[v] = depart

    # on change les scores des villes
    # tant qu'il y a des villes à voir et qu'on est pas arrivé
    # à destination
    n = 0
    while len(villes_a_voir) > 0:
        # on cherche la ville à voir qui a le plus petit score
        ville_actuelle = villes_a_voir[0]
        i = 0
        for j in range(len(villes_a_voir)):
            if score[villes_a_voir[j]] < score[ville_actuelle]:
                ville_actuelle = villes_a_voir[j]
                i = j
        # on considère cette ville comme vue
        villes_a_voir.pop(i)
        villes_vues.append(ville_actuelle)
        # on regarde toutes les voisines
        # de la ville actuelle
        for v in graphe[ville_actuelle]:
            if v not in villes_vues:
                # je calcule son score par ce chemin
                s = score[ville_actuelle] + graphe[ville_actuelle][v]
                if v not in score or s < score[v]:
                    score[v] = s
                    precedente[v] = ville_actuelle
                if v not in villes_a_voir:
                    villes_a_voir.append(v)
    #        n+=1
    #        print("Etape ",n)
    #        print("ville_actuelle:",ville_actuelle)
    #        print(score)
    #        print()
    # on a terminé la recherche, il reste à reconstruire
    # le chemin trouvé
    chemin = [arrivee]
    ville_actuelle = arrivee
    while ville_actuelle != depart:
        ville_actuelle = precedente[ville_actuelle]
        chemin.append(ville_actuelle)
    return chemin[::-1]


print("Trajet Rennes-Lyon")
print(dijkstra(carte, "Rennes", "Lyon"))
print()
print("Trajet Strasbourg-Bordeaux")
print(dijkstra(carte, "Strasbourg", "Bordeaux"))
