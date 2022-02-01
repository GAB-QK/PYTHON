# -*- coding: utf-8 -*-

"""
Voici un récapitulatif de ce qu'on a vu a propos de python

N'essayez pas d'executer ce fichier, ca ne marchera pas.
En revanche, vous pouvez copier-coller les morceaux interessants dans votre code.
"""


"""
Les différents types
"""

# 1. Les nombres.
# Toutes les expressions suivantes sont des nombres:
2
-4
5.3
7+1
5.7/2
int("5") #convertit une chaine de caracteres en nombre entier

# 2. Les chaînes de caracteres
"Bonjour"
"Bonjour " + "Monsieur"
""
str(4)  #convertit un nombre en chaine de caracteres
"Bonjour\n" # \n represente un retour a la ligne


# 3. Les Booleens
True
False
5>2
4<=0
"abc" == "abc"
5>2 and 3<=8
3>0 or 3<0
not 7==6

# 4. Les listes
[1,2,3]
[]
["a","b","c","d"]
[1,2] + [3,4]

"""
Les variables
"""

#on assigne une valeur à une variable avec le signe =
a=2
b=5
c="Bonjour"
l1=[5,4,7]
l2=[3,2,1]

#on peut faire des operations sur les variables
x=a+b
l3=l1+l2

"""
Interactivite
"""

#pour afficher quelque chose dans la console
print(12)
print("Bonjour")
print(a)

#pour demander a l'utilisateur de rentrer une valeur au clavier
texte=input("Entrez un texte et appuyez sur Entree.")
valeur=int(input("Entrez un nombre:"))

"""
Manipulation de listes
"""

#Les elements d'une liste sont numerotes a partir de zero
l1[0] # premier element
l1[-1] #dernier element
l3[1:4] #liste contenant les elements d'indices 1,2 et 3 de la liste l3
l3[2:] #liste contenant tous les elements de l3 a partir du troisieme
l3[::-1] #liste renversee
l3[::2] #un element sur deux


"""
Branchement conditionnel
"""

if a>2:
    print("a est superieur a 2")


if a>0 and b>0:
    print("a et b sont positifs")
else:
    print("a et b ne sont pas tous les deux positifs")


if a>100:
    print("a est grand")
elif a>10:
    print("a est moyen")
elif a>0:
    print("a est petit")
elif a==0:
    print("a est nul")
else:
    print("a est negatif")


"""
fonctions
"""

#exemples de fonctions sans arguments
input()
random.random() #ne pas oublier d'importer le module random

#fonctions a 1 argument
int("7")
time.sleep(1) #ne pas oublier d'importer le module time

#fonctions a 2 arguments
min(0,8)
max(0,8)

#si une fonction renvoie une valeur, on peut assigner celle-ci a une variable
a=input()
m=max(0,8)
sept=int("7")

#definition d'une fonction
def mafonction(argument1,argument2):
    resultat=argument1+argument2*argument2
    return resultat

#fonction sans argument
def tete_a_toto():
    return 0


"""
modules
"""

#2 facons d'importer un module
import time
time.sleep(2)

#ou bien
from time import *
sleep(2)


"""
boucle while
"""

a=10
while a>=0:
    print("a=",a)
    a=a-1

#Le bloc suivant demande d'entrer des nombres jusqu'a tomber sur zero
on=True
while on:
    n=int(input("Entrez un nombre:"))
    on=n!=0 #la variable booleene on vaudra True si n est different de zero, False si n==0
    
"""
boucle for
"""

for element in [7,8,4,9,5]:
    print(element*element)
    
for i in range(5):
    print(i)
    
for i in range(5,-1,-1):
    print(i)
    
"""
Fichiers
"""

#ecrire dans le fichier monfichier.txt
with open("monfichier.txt","w") as monfichier:
    monfichier.write("ligne1\n")
    monfichier.write("ligne2\n")
    
#lire un fichier en entier
with open("monfichier.txt","r") as monfichier:
    contenu=monfichier.read()
    
#lire la premiere ligne d'un fichier
with open("monfichier.txt","r") as monfichier:
    ligne1=monfichier.readline()

"""
Classes
"""

class nomclasse(classemere):
    #constructeur
    def __init__(self,parametre):
        #appel du constructeur de la classe mere
        super().__init__(self)
        #attributs propres à cette classe
        self.i=0
        self.param=parametre
        
    #methode
    def methode(self,x):
        return self.parametre+x
    
#Création d'une instance
moninstance=nomclasse(4)
print(moninstance.methode(7))


"""
Interface graphique (module tkinter)
"""

#création d'une fenetre
fenetre=tk.Tk()

#widgets
tk.label(fenetre,text="blabla")
tk.Button(fenetre,text="blabla",command=fonction_a_appeler)
tk.Entry(fenetre,textvariable=ma_string_var)
tk.Canvas(fenetre,width=400,height=300)

#placement d'un widget
widget.grid(row=2,column=3,rowspan=2,columnspan=2)

#Dessin dans un canvas
canvas.create_line(x1,y1,x2,y2)
canvas.create_rectangle(x1,y1,x2,y2)
canvas.create_oval(x1,y1,x2,y2)

#réagir au clic dans un canvas
canvas.bind("<button-1>",fonction_a_appeler)


"""
module numpy
"""

#creation d'un array
a=np.array([1,2,3])
a=np.arange(2,8,2)
a=np.linspace(1,10,40)
a=np.zeros((6,7))
a=np.ones((6,7))
identite=np.eye(4)

#indexation
print(identite[1,2])

#les operations s'effectuent sur chaque élément
print(a+2)

