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
