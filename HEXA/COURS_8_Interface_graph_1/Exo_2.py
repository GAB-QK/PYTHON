import tkinter as tk
import webbrowser as wb


# on crée une nouvelle fenêtre
fenetre = tk.Tk()

# les éléments d'une fenêtre s'appelle des widget


nombre_clics = 0    # variable init

# fonction qui modifie le texte du label
def modifie_label():
    global nombre_clics
    nombre_clics+=1
    Texte="nombre de clic :",str(nombre_clics)
    mon_label.config(text=Texte)

def Reset():
    global nombre_clics
    nombre_clics=0
    Texte="nombre de clic",str(nombre_clics)
    mon_label.config(text=Texte)

def secret():
    wb.open('https://docs.python.org/fr/3/library/tkinter.ttk.html#widget')

#widget  bouton

mon_label = tk.Label(text=
                     "Clique sur le bouton.\n vise bien !")
mon_bouton =tk.Button(fenetre,text="Clique ici",
                      command=modifie_label)
Bouton_Reset =tk.Button(fenetre,text="Reset",
                        command=Reset)
Bouton_secret =tk.Button(fenetre,text="allez mon cochon !",
                         command=secret)
Label_2 =tk.Label(text=
                  "je suis seul")



# on place le  widget  sur  la  fenetre
# premier widget : le label
# Affichage
mon_label.grid(row=0,column=0,columnspan=3) # affiche un texte à l'écran
mon_bouton.grid(row=1,column=1)
Bouton_Reset.grid(row=1,column=2)
Label_2.grid(row=3,column=3)
#Bouton_secret.grid(row=2,column=0,columnspan=2)  # column span signifie que le widget va prendre deux colonne de large



tk.mainloop()