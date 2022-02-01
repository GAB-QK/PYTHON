""""""

from sympy import *
import tkinter as tk
"""
EXO
Ecrire une fonction qui prend en parametre une fonciton f,
sa dérivée, une valeur de départ a0 et uine précision epsilon et qui  renvoie une valeur approchée
d'une solution de l'équation f(x) = 0
Tester cette fonction avec la fonctino hci dessus 
"""

def h(x):
    return -x**3 + 3*x**2 + 40

def hprime():
    x = Symbol('x')
    y = h(x)
    yprime = y.diff(x)
    return yprime

def tangente(fonction, derive, a0, epsilon):
   x = a0
   n = 0
   while abs(fonction(x)) > epsilon:
       x = x - fonction(x) / derive(x)
       n += 1
   return x, n
xh3, nh3 = tangente(h, hprime, 10, 1.e10)
print(xh3, h(xh3), nh3, "iterations")


"""
l'equation de la tangente à la courbe de f en a s'écrit : 
y = f'(a)(x-a)+f(a)         de la forme y =mx+p

Ainsi, à partir de la tangente en "an" on trouve le point an+1 par 
f'(an)* ( an+1 -an) + f(an) = 0
an+1 - an = (f(an) / f'(an))
an+1 = an - (f(an) / f'(an))
"""
def affichage():
    fenetre = tk.Tk()

    photo = tk.PhotoImage(file='IMAGE/CP_ECRAN_2.png')

    label = tk.Label(fenetre, image=photo)
    label.pack()

    fenetre.mainloop()
affichage()