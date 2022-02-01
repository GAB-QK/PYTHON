""" resolution d'une equation """


def f(x):
    return x ** 3 - 5 * x ** 2 + 3


# precision que l'on veut atteindrte
epsilon = 1e-10

"""le tableau de variation de la fonction nous indique une fois 
dans l'intervalle [0;10/3]"""

print(f(0), f(10 / 3))

"""
premiere methode : Dicotomie
on divise l'intervalle en deux parties égales 
"""


x = (0 + 10 / 3) / 2  # on on prend le milieu de l'intervalle
y = f(x)
print("y=", y)
erreur = abs(y)
if erreur > epsilon:
    # on regarde dans quelle moitiée d'intervalle on veut continuer la recherche
    if y > 0:
        a = 0
        b = x
    else:
        a = x
        b = 10 / 3
    x = (a + b) / 2
    y = f(x)
    erreur = abs(y)
    if erreur > epsilon:
        # on regarde dans quelle moitiée d'intervalle on veut continuer la recherche
        if y > 0:
            b = x
        else:
            a = x
