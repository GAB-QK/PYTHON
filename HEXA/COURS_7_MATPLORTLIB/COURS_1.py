'''Exo
tracer les courbes représentative des fonctions
f(x)=x^2+1, g(x)=x^2 et h(x)=x^2+3
sur l'intervalle [-5,5]'''

'''Exo
tracer la trajectoire d'un point partant de l'origine à l'instant t=0 et dont les 
coordonnées évoluent au cours du temps suivant les fonctions : 
    XT(t)=3t
    YT(t)=t^2
jusqu'à t=10
'''

import matplotlib.pyplot as plt
def g(x):
    return x**2-2
def h(x):
    return x**2+3
def f(x):
    return x**2+1

X =[]
Y =[]
GY =[]
HY =[]

for i in range (-5,6) :
    X.append(i)
    Y.append(f(i))
    GY.append(g(i))
    HY.append(h(i))
plt.plot(X, Y,label="f(x)")
plt.plot(X, GY,label="g(x)")
plt.plot(X, HY,label="h(x)")
plt.legend()
plt.show()


XT =[]
YT =[]


def T(xt):
    return xt**2

for i in range (0,11):
    XT.append(3*i)
    YT.append(T(i))
plt.plot(XT,YT,label="T(x)")
plt.legend()
plt.show()


