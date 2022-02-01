""""""
"""
Exo
Exprimer x en fonction de a et de b et f(a) et f(b)
"""
def g(x):
    return -x ** 5 + 4 * x ** 4 + 100 * x + 30

def calculer_Coef_directeur(xa, ya, xb, yb):        # calcul du coef directeur
    deltaX = xb-xa
    deltaY = yb-ya
    return deltaY/deltaX

def calculer_P(xa, ya, xb, yb):                     # calcul du point à l'origine
    m = calculer_Coef_directeur(xa, ya, xb, yb)
    p = ya-m*xa
    return p

def X0(m, p):                               # resolution d'equation du premier degré pour mx+p=r
    A = 0 - p
    solution = A / m
    return solution

"""
Deuxième methode 
methode des sécante 
on dvise l'intervalle en partie inégales
en utilisant la droite qui psse par (a,f(a)) et (b,f(b)) et en coupant à l'intersection 
de cette droite avec l'axe des abscisse 
"""

def decante(fonction,a,b,epsilon):
    gauche = a
    droite = b
    m = calculer_Coef_directeur(gauche, fonction(gauche), droite, fonction(droite))
    p = calculer_P (gauche, fonction(gauche), droite, fonction(droite))
    x = X0(m,  p)
    y = fonction(x)
    n = 0  # pour compter le nomre d'iteration
    while abs(y) > epsilon:
        # si fonction(a) et y ont le même signe
        # alors on garde l'intervalle de droite
        if fonction(a) * y > 0:  # on garde l'intervalle de droite
            gauche = x
        else:  # on garde l'intervalle de gauche
            droite = x
        x = X0(m, p)
        y = fonction(x)
        n += 1
    return x, n

xg1, ng1 = decante(g, -2, 2, 1.e-10)
print("decante: ", xg1, g(xg1), ng1)

