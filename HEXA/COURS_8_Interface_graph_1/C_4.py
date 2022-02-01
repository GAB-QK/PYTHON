import tkinter as tk78

fenetre=tk78.Tk()

label=tk78.Label(fenetre,text="NOM?")
label.grid(row=0,column=0)

#StringVar est une variable equivalente à une string mais ui est mise à jour
# par certain widgets
nom=tk78.StringVar()
#troisieme widget / Entry
entree=tk78.Entry(fenetre,textvariable=nom)
entree.grid(row=0,column=1)

label2=tk78.Label(fenetre,textvariable=nom)
label2.grid(row=1,column=0,columnspan=2)

tk78.mainloop()
