""""""
import tkinter as tk
def affichage():
    fenetre = tk.Tk()

    photo = tk.PhotoImage(file='IMAGE/CP_ECRAN_1.png')

    label = tk.Label(fenetre, image=photo)
    label.pack()

    fenetre.mainloop()
affichage()
"""
La méthode de la tengante consiste à partir d'un poiont a0 et de tracer la tangeante à la courbe de f en a0.
cette tangente coupe l'axe des abscisses en  an. On peut répéter l'operation 
pour obtenir une suite ( a0,a1,a2,...,an,... de positions

En general, cette suite  converge vers un zero de de la focntion

Remarque : pour utiliser cette methode la fonction doite être continue et derivable 
et on doit connaitre sa dérivé 
"""


"""
l'equation de la tangente à la courbe de f en a s'écrit : 
y = f'(a)(x-a)+f(a)         de la forme y =mx+p

Ainsi, à partir de la tangente en "an" on trouve le point an+1 par 
f'(an)* ( an+1 -an) + f(an) = 0
an+1 - an = (f(an) / f'(an))
an+1 = an - (f(an) / f'(an))"""