import tkinter as tk
import numpy as np
import random as r


'''afficher une fenetre avec  un canvas contenant une grille et unlabel sous le canvas
 qui affiche le nombre de mine '''
class Demineur:
    def __init__(self,nb_lignes,nb_colonnes,taille_case,nb_mines):

        self.nb_lignes=nb_lignes
        self.nb_colonnes=nb_colonnes
        self.taille_case=taille_case
        self.nb_mines=nb_mines
        self.marge=5

        self.fenetre=tk.Tk()
        self.fenetre.title("demineur")

        ##############################################################

        #fond du jeu
        self.canvas = tk.Canvas(self.fenetre, width=self.nb_colonnes * self.taille_case, height=self.nb_lignes * self.taille_case, background="white")
        self.canvas.grid()

        #ligne du jeu (plateau de jeu)
        self.init_grille(self.nb_lignes,self.nb_colonnes,self.canvas,self.taille_case)
        self.canvas.grid()


        #creation matrice
        self.Grille = np.zeros((self.nb_lignes, self.nb_colonnes))
        self.COPY = self.Grille.copy()

        # apelle spawn mine
        self.spawn_mine(self.nb_mines,self.nb_lignes,self.nb_colonnes)
        print(self.Grille)

        # apelle bind bouton gauche
        self.canvas.bind("<Button-1>", self.Clic)
        tk.mainloop()

    #############################################################
    # création des grilles
    def init_grille(self,NL,NC,C,TC):
        for i in range(self.nb_lignes):
            C.create_line(0,i*TC,TC*NC, i*TC, width=2,fill="black")
        for i in range(self.nb_colonnes):
            C.create_line(i*TC,0, i*TC, TC *NL, width=2,fill="black")

    #Methode case
    def case(self,x, y):
        return y // self.taille_case, x // self.taille_case
    #Methode coordonnees
    def coordonnees(self,ligne, colonne):
        return colonne * self.taille_case, ligne * self.taille_case


    #Methode clic
    def Clic (self,event):
        ligne, colonne = self.case(event.x,event.y)
        x,y = self.coordonnees(ligne,colonne)
        print(self.Grille,"\n")
        print(ligne,colonne)


        if self.Grille[ligne, colonne] == -1 :
            self.Rond(x,y)
            self.canvas.unbind("<Button-1>")
            self.Gros_looser()

        else:
            if self.COPY[ligne,colonne] == 0:
                self.canvas.create_text((colonne*self.taille_case)+self.taille_case//2,(ligne*self.taille_case)+self.taille_case//2,
                                        text=str(int(self.Grille[ligne][colonne])),fill="black")
                self.COPY[ligne][colonne] = 1
                self.canvas.grid()

            return ligne, colonne
    # methode spawn des mines
    def spawn_mine(self,nb_mines,Limite_y,Limite_x):
        j=0
        while j < nb_mines :
            xm = r.randint(0, self.nb_colonnes-1)
            ym = r.randint(0, self.nb_lignes-1)
            if self.Grille[ym][xm] == 0:
                self.Grille[ym][xm] = -1
                j += 1
        for y in range (0,Limite_y):
            for x in range (0,Limite_x):
                self.chek_bomb(x,y)
############################################################
# methode bomb chek
    def chek_bomb(self,Xcb,Ycb):
        if self.Grille [Ycb][Xcb] == 0:
            bombfound = 0
            for y in range (-1,2):
                for x in range (-1,2):
                    try :
                        if self.Grille[Ycb+y][Xcb+x]==-1 and Ycb+y >=0 and Xcb+x >= 0:
                            bombfound+=1
                        else:
                            continue
                    except:
                        continue
            self.Grille[Ycb][Xcb] = bombfound

############################################################
# affichage canva/ligne/code
    def fenetre(self):
        self.label=tk.Label(self.fenetre,text=self.nb_mines)
        self.label.grid(row=0,column=0)
    def Rond(self,x,y):
        self.canvas.create_oval(x+self.marge,y+self.marge,x+self.taille_case-self.marge,y+self.taille_case-self.marge,fill="red")
        self.canvas.grid()
    def Gros_looser(self):
        self.label = tk.Label(self.fenetre, text="ALLAH OU AKBAR MON LOULOU ")
        self.label.grid(row=0, column=0)

############################################################
Demineur=Demineur(8,16,30,20)


