'''
Exercice
créer un canvas blanc carré divisé en une grille 3x3 par des lignes noires

Ecrire  une fonction qui prend en parametre deux coordonnées x et y et qui trace une croix bleu de la taille
d'une case et dont l'extremite  en haut àgauche  est  la position x,y

Ecrire une fonction qui prned en parametre eux coordonnnées x et y et quitrace en cercle rouge de la taille
d'une case et dont l'extremité en haut à gauche ddu rectangle circonscrit
'''

import tkinter as tk
import numpy as morgane
from SIRI import *
###############################################################
# variable et import

fenetre=tk.Tk()
fenetre.title("Jeu_Canva")
taille =100
marge = 20
grille=morgane.zeros((3,3))       #matrice de 3*3 pour pas jouer deux fois au même endroit
tour = 0

###############################################################
# def des fonctions
def Case (x,y):
    if x<taille:
        colonne=0
    elif x<2*taille:
        colonne=1
    else:
        colonne=2
    if y<taille:
        ligne=0
    elif y<2*taille:
        ligne=1
    else:
        ligne=2
    return (ligne,colonne)


def Coord_case(ligne,colonne):
    if ligne == 0:
        y=0
    elif ligne== 1:
        y=taille
    else:
        y=2*taille
    if colonne == 0:
        x = 0
    elif colonne == 1:
        x = taille
    else:
        x = 2 * taille
    return(x,y)

def croix (x,y):
    canvas.create_line(x+marge,y+marge, x+taille-marge, y+taille-marge, width=3, fill="blue")
    canvas.create_line(x + marge, y +taille -marge, x +taille-marge, y + marge, width=3, fill="blue")
def cercle (x,y):
    canvas.create_oval(x+marge,y+marge,x+taille-marge,y+taille-marge, width=3, outline="red")

def alignement (ligne,colonne):
    if grille [ligne,0]==grille[ligne,1]==grille[ligne,2]:
        return True
    if grille [0,colonne]==grille[1,colonne]==grille[2,colonne]:
        return True
    if grille[0,0] == grille[1,1] == grille[2,2]:
        return True
    return False

def clic_G (evenement):
    global tour
    # on trouve dans quelle case le joueur a cliqué
    ligne, colonne = Case(evenement.x, evenement.y)
    # on teste si la case est libre
    if grille[ligne, colonne] == 0:
        x, y = Coord_case(ligne, colonne)
        croix(x, y)
        grille[ligne, colonne] = 1
        txtjoueur = "croix"
        if alignement(ligne, colonne):
            label.config(text="Victoire du joueur " + txtjoueur)
        elif tour == 8:
            label.config(text="Match nul !")
        else:
            tour += 1
            canvas.unbind("<Button-1>")

            # au tour de l'ordi
            ligne, colonne = ordi.joue(grille.copy())
            x, y = Coord_case(ligne, colonne)
            cercle(x, y)
            grille[ligne, colonne] = 2
            txtjoueur = "rond"
            if alignement(ligne, colonne):
                label.config(text="Victoire du joueur " + txtjoueur)
            elif tour == 8:
                label.config(text="Match nul !")
            else:
                canvas.bind("<Button-1>", clic_G)
                tour += 1


###############################################################
# background jeu
canvas=tk.Canvas(fenetre,width=300,height=300,background="white")
ordi=SIRI_himar(2)
###############################################################
# decla fonction des bouton
canvas.bind("<Button-1>",clic_G)
##############################################################
#ligne du jeu (plateau de jeu)
canvas.create_line(100, 0, 100, 300, width="10", fill="black")
canvas.create_line(200, 0, 200, 300, width="10", fill="black")
canvas.create_line(0, 100, 300, 100, width="10", fill="black")
canvas.create_line(0, 200, 300, 200, width="10", fill="black")
label=tk.Label(fenetre,text="Morpion")
label.grid(row=1,column=0)
###############################################################
# affichage

canvas.grid()
tk.mainloop()