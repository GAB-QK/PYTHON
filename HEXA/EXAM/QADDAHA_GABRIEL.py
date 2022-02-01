PARTIE 1 :

Question 1 :
B:120

Question 2:
B: 0

question 3:
C : Mettre une condition après else

question 4:
C : (x+2)2

question 5:
C:6

question 6:
C : « Bonjour » à l’infini

question 7:
B : Les nombres de 1 à 99 sauf les dizaines

question 8:
A : La somme des éléments d’une liste

question 9:
D : Une erreur

question 10:
C : 13131

PARTIE 2 :

Question 1 :

def morgane (A,B):
    if  A%B:
        print(False)
    else:
        print(True)

morgane(981,9)
morgane(47,4)

Question 2 :

import  random as r

def morgane (N):
    liste=[r.randint(1,10) for i in range (N)]
    print(liste)

morgane(3)

Question 3 :


A=0
B=0
while A>=0 and B<5:
    A=int(input("c'est quoi le nombre stp ?"))
    B+=1

Question 4:

import random as r


with open("EXAM.txt", "w") as fichier:
    for i in range(5):
        liste = [r.randint(1, 10) ]
        fichier.write(str(liste))
        fichier.write("\n")
    fichier.close()

Question 5 :

A="c'est quoi le niveau de style sur 10 de thomas.H ? "
B=10    # la variable B represente la bonne réponse, pour plusieurs reponses possibles on aurait pu faire une
        #liste qu'on parcoure et verifier si la réponse existe dedans ou non
Reponse_user = int(input(A))        # le user entre sa réponse

if Reponse_user == B:       # verification de l'égalité avec la bonneréponse
    print("bonne réponse")  #  si  oui afficher bonne réponse
else:
    print("Faux,la bonne réponse etait :",B)     # sinon afficher faux et la réponse attendu

Question 6:

import tkinter as tk
import random as r
#fenetre
fenetre = tk.Tk()
# variable marge
marge = 20
###############################################################
# fonction
def cercle ():
    x=r.randint(0+marge,600-marge)
    y=r.randint(0+marge,300-marge)
    canvas.create_oval(x,y,x+20,y+20, width=3, outline="red")

###############################################################
#widget
mon_bouton =tk.Button(fenetre,text="Clique surprise",
                      command=cercle)

mon_label = tk.Label(text=
                     "Question 6")

canvas=tk.Canvas(fenetre,width=600,height=300,
                 background="white")
###############################################################
#Affichage grid
mon_label.grid()
canvas.grid()
mon_bouton.grid()
###############################################################
#main loop
tk.mainloop()











