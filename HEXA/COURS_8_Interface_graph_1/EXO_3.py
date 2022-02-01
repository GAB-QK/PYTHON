import tkinter as tk
'''Exo
créer un programme qui demande un identifiant et un mtp
avec un bouton ok et un label qui  affiche qui es tu ?
si thibaut  et mdp azeerty et clique sur ok le label doit afficher bienvenu thibaut
si ToTo  entre mdp toto et  clique sur ok bienvenu toto
si BOB entre mdp  éponge afficher bienvenue BOB
si on ne connait pas le mdp label affiche mdp incorrect si utilisateur inconnue
 le label utilisateur inconnu'''


fenetre=tk.Tk()
fenetre.title("Connexion")
fenetre.geometry("400x150")

User=tk.StringVar()     #créa de string var user et mdpqu'on conveertie en str avec get
Mdp=tk.StringVar()
dico_User_Mdp ={"Thibaut":"azerty",
                "BOB":"eponge",
                "TOTO":"toto"}    # dico des user(key) et mdp(value)
#def de fonction
def ok ():
    global User
    global Mdp

    if User.get() in dico_User_Mdp :
        if Mdp.get() == dico_User_Mdp[User.get()] : #verifie la value des clés
            label_Q.config(text=("bienvenue",User.get()))   #  utilisation du get permet de convertir string
        else:
            label_Q.config(text="mdp incorect ")
    else:
        label_Q.config(text="User incorect")

def init():
    global User
    global Mdp
    dico_User_Mdp[User.get()]= Mdp.get()
    print (dico_User_Mdp)

def aff_mdp():                   # fonction appellé par le bouton afficher mdp et remet ensemble
    entree_MDP.config(show="")     # vide par le remplacement de  caractère

def palestine():
    label_Q.config(text="vive la palestine")




#########################################################################
#création de tous les labels
label_U=tk.Label(fenetre,text="Utilisateur ?")
label_U.grid(row=0,column=1)
label_M=tk.Label(fenetre,text="MDP  ?")
label_M.grid(row=1,column=1)
label_Q=tk.Label(fenetre,text="Qui est tu ?")
label_Q.grid(row=3,column=2,columnspan=2)
#########################################################################
#création de mes entrée
entree_user=tk.Entry(fenetre,textvariable=User)
entree_user.grid(row=0,column=2)
entree_MDP=tk.Entry(fenetre,textvariable=Mdp,show="*")      # cache l'affiche du mdp
entree_MDP.grid(row=1,column=2)
########################################################################
#création des boutons
Bouton_OK =tk.Button(fenetre,text="OK!",
                         command=ok)
Bouton_init =tk.Button(fenetre,text="add user",
                       command=init)
Bouton_Aff_Mdp =tk.Button(fenetre,text="affichere mdp",     #bouton pour afficher le mdp
                          command=aff_mdp)
Bouton_hassoun= tk.Button(fenetre,text="hassoun",
                          command=palestine)
#########################################################################
#affichage bouton
Bouton_OK.grid(row=0,column=4)
Bouton_init.grid(row=1,column=4)
Bouton_Aff_Mdp.grid(row=4,column=2)
Bouton_hassoun.grid(row=5,column=2)


tk.mainloop()
