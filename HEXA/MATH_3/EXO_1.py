def f(x):
    return x ** 3 - 5 * x ** 2 + 3


def g(x):
    return -x ** 5 + 4 * x ** 4 + 100 * x + 30


"""
le tableau de variation de la focntion nousindique qu'elle s'annule une fois dans l'intervalle
[0;10/3]
"""
epsilon = 1e-10
a = 0
b = 10 / 3
print(f(a), f(b))

"""
EXO
afficher le milieu de [a;b] et son image par la fonction f
"""

x = (a + b) / 2
print(x)

"""
EXO_2
ecrire une fonction qui prend en parametre les bornes a et b et la precision epsilon et qui calcule
le milieu de x de [a;b] et son image f, la fonction renvoie TRUE si l'image est suffisamment 
petite ( si sa valeur absolue est inferieur à epsilon
"""


def Dichotomie(a, b, epsilon):
    x = (a + b) / 2
    y = f(x)
    return abs(y) < epsilon


# print(Dichotomie(0,10/3,epsilon))
# print(Dichotomie(0,10/3,15))


"""
EXO_3
modifié la fonction precente pour qu'elle divise une deuxcième fois l'intervalle et teste si l'image du milieu est 
suffisamment proche de 0 
"""


def Dichotomie_2(a, b, epsilon):
    gauche = a
    droite = b
    x = (gauche + droite) / 2
    y = f(x)
    while abs(y) > epsilon:
        if y > 0:  # on garde l'intervalle de droite
            gauche = x
        else:  # on garde l'intervalle de gauche
            droite = x
        x = (gauche + droite) / 2
        y = f(x)
    return x


x_min = Dichotomie_2(0, 10 / 3, 1.e-10)

print(x_min, f(x_min))


def Dicotomie_3(fonction, a, b, epsilon):
    gauche = a
    droite = b
    x = (gauche + droite) / 2
    y = fonction(x)
    n = 0  # pour compter le nomre d'iteration
    while abs(y) > epsilon:
        # si fonction(a) et y ont le même signe
        # alors on garde l'intervalle de droite
        if fonction(a) * y > 0:  # on garde l'intervalle de droite
            gauche = x
        else:  # on garde l'intervalle de gauche
            droite = x
        x = (gauche + droite) / 2
        y = fonction(x)
        n += 1
    return x


print(g(-2), g(2))
xg1, ng1 = Dicotomie_3(g, -2, 2, 1.e-10)
print("dicotomie: ", xg1, g(xg1), ng1)
