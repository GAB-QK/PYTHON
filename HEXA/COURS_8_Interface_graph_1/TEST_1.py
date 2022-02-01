import tkinter as tk
import webbrowser as wb


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
    mon_label.config(text=Texte)

def Reset():
    global nombre_clics
    nombre_clics=0
    Texte="nombre de clic",str(nombre_clics)
    mon_label.config(text=Texte)

def secret():
    wb.open('https://docs.python.org/fr/3/library/tkinter.ttk.html#widget')

#widget  bouton


mon_bouton =tk.Button(fenetre,text="Clique ici",
                      command=modifie_label)
Bouton_Reset =tk.Button(fenetre,text="Reset",
                        command=Reset)
Bouton_secret =tk.Button(fenetre,text="allez mon cochon !",
                         command=secret)


mon_bouton.grid()
Bouton_Reset.grid()
Bouton_secret.grid()

tk.mainloop()