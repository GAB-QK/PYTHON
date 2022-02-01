'''dictionnaire qui  represente les positions de plusieurss points'''

positions={"A":[3,5],"B":[-2,0],"C":[5,0],"D":[0,3],"E":[-4,-1],"F":[-2,2]}

'''exercice 
afficher la distance entre les points B et E'''

import math as m
import random as groot

def distance(D):
    xB,xE,yB,yE =  D["B"][0],D["E"][0],D["B"][1],D["E"][1]
    return m.sqrt(((xB-xE)**2)+((yB-yE)**2))

'''
                                    "solution prof "
    DX=position["B"][0]-positions["E"][0]
    DY=positions["B"][1]-positions["E"][1]
    dist=m.sqrt(DX**2+DY**2)
    print(dist)
    
    '''

print(distance(positions))


'''Exo
    Ecrire une fonction qui prend en parametre un nombre n et qui renvoie un dico similaire à cleui-ci mais avec n points A,B et C
etc.. et des coordonnées entières tirées au hasard dans l'intervalle [-5;5]'''

def thomasGenerator2003(n):
    NewDico = {}
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range (n):
        NewDico[alpha[i]] = [groot.randint(-5,5),groot.randint(-5,5)]
    return NewDico
#print(thomasGenerator2003(5))
Ndico = thomasGenerator2003(5)


'''exo
ecrire une fonction qui prend en parametre un dico de coordonnées de pts te une chaine de caractère representant un segment
par exemple "AB" et qui renvoie la longueur du segment '''

def distance2(D,XA,XB):
    Key1,Key2=list(D.items())[XA][0],list(D.items())[XB][0]
    x1,x2,y1,y2=D[Key1][0],D[Key2][0],D[Key1][1],D[Key2][1]
    return  m.sqrt(((x1-x2)**2)+((y1-y2)**2))




print(Ndico)
print(distance2(Ndico,1,2))

'''                     solution prof                   '''

def liste_point(d,n1,n2):
    return m.dist(d[n1],d[n2])





