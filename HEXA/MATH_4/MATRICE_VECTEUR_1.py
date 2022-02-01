# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


class Dessin:
    def __init__(self, coord, boucle=True):
        # on crée une liste de traits
        # un trait est une ligne continue
        self.trait = []
        self.nb_points = 0
        self.est_une_boucle = []
        self.ajouter_trait(coord, boucle)

    '''
    Ajoute un trait (une ligne continue)
    à la liste à partir d'une liste de coordonnées
    de points
    Si boucle=True, le dernier point est relié au premier
    '''

    def ajouter_trait(self, coord, boucle=True):
        self.trait.append(coord)
        self.nb_points += len(coord)
        self.est_une_boucle.append(boucle)
        if boucle:
            # on ajoute les coordonnées du
            # premier point à la fin du trait
            # pour revenir au point de départ
            self.trait[-1].append(coord[0])
        self.trait[-1] = np.array(self.trait[-1], dtype=float)

    '''
    Dessine tous les traits
    '''

    def draw(self):
        for t in self.trait:
            x = t[:, 0]
            y = t[:, 1]
            plt.plot(x, y)
        plt.gca().set_aspect('equal')

    def translation(self, a):
        for t in self.trait:
            t += a

    def centre(self):
        resultat = np.zeros(2, dtype=float)
        for i in range(len(self.trait)):
            # x et y sont les coordonnées du traits
            x = self.trait[i][:, 0]
            y = self.trait[i][:, 1]
            # si le trait est une boucle
            # on retire le dernier point du calcul
            if self.est_une_boucle[i]:
                resultat[0] += sum(x[:-1])  # on enelève le dernière elements comme c'est une boucle
                resultat[1] += sum(y[:-1])  # (repetition du 1ER elements sinon )
            else:
                resultat[0] += sum(x)
                resultat[1] += sum(y)
            # on renvoie la moyenne des abscisse et des ordonnées
        return resultat / self.nb_points  # on divise par le nombre de points

    def agrandissmeent(self, a):
        c = self.centre()
        # on recentre le trait sur l'origine
        self.translation(-c)
        for t in self.trait:
            # on multiplie toute les coord par a
            t *= a
        self.translation(c)  # on replace le trait au bon endroit

    def rotation_origine(self,theta):
        for t in self.trait:
            for i in range(len(t)):
                x = t[i, 0]*np.cos(theta)-t[i, 1]*np.sin(theta)
                y = t[i, 1]*np.cos(theta)+t[i, 0]*np.sin(theta)
                t[i]=np.array([x, y], dtype=float)

    def rotation(self,point,theta):
        self.translation(-point)
        self.rotation_origine(theta)
        self.translation(point)

    def transformation(self,matrice,origine=np.zeros(2,dtype=float)):
        self.translation(-origine)
        for t in self.trait:
            for i in range(len(t)):
                t[i] = np.dot(matrice,t[i])
        self.translation(origine)


################################################################################################
################################################################################################
# AFFICAHGE des figure et execution des methodes

triangle1 = Dessin([[0, 1], [2, 2], [3, 1]])
triangle1.draw()

pentagone1 = Dessin([[0, 0], [1, 0], [1, 1], [-1, 2],
                     [-2, -2]])
pentagone1.ajouter_trait([[0, 0.5], [-0.5, 1], [-1, 0]])
pentagone1.draw()

'''
Exercice
Dessiner une maison avec une fenetre
'''


maison1 = Dessin([[2, 3], [2, 0], [6, 0], [6, 3],           # MAISON ET TOIT
                  [2, 3], [4, 5], [6, 3]], boucle=False)

maison1.ajouter_trait([[4.5, 1.5], [5, 1.5], [5, 2], [4.5, 2]])     # FENETRE
maison1.draw()

maison1.translation(np.array([5, 3]))
maison1.draw()

c = maison1.centre()
plt.plot([c[0]], [c[1]], "kx")

maison1.agrandissmeent(1.5)
maison1.draw()

# rotation du pentagone
pentagone1.rotation_origine(np.pi/2)
pentagone1.draw()

maison1.rotation(maison1.centre(),np.pi/2)
maison1.draw()
plt.show()
