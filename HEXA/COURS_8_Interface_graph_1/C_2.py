import tkinter as tk

# on crée une nouvelle fenêtre

fenetre = tk.Tk()

# les éléments d'une fenêtre s'appelle des widget
# premier widget : le label
# affiche un texte à l'écran

mon_label = tk.Label(text=
                     "Clique sur le bouton.\n vise bien !")

#onplace le  widget  sur  la  fenetre
mon_label.grid()
# fonction qui modifie le texte du label

nombre_clics = 0

def modifie_label():
    global nombre_clics
    nombre_clics+=1
    Texte="nombre de clic :",str(nombre_clics)
    mon_label.config(text=Texte)        # modification de texte

#widget  bouton
mon_bouton =tk.Button(fenetre,text="Clique ici",
                      command=modifie_label)
mon_bouton.grid()
tk.mainloop()