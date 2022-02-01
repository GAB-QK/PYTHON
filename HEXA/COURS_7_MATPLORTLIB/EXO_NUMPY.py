''' Exo
dessiner unee petite maison avec matplotliob
'''

'''
Exo
Ecrire une fonction rotation qui prend en parametree un angle
 en degrés et qui renvoie la matrice de rotation correspondante
 Une matrice de rotation '''

'''dessiner l'image de la maison par rotation 
d'un angle de  45°'''

import matplotlib.pyplot as plt

XA=[1,8]
YA=[8,8]

XB=[8,1]
YB=[1,1]

XC=[1,1]
YC=[8,1]

XD=[8,1]
YD=[8,8]

plt.plot(XA,YA,label=("H"))
plt.plot(XB,YB,label=("B"))
plt.plot(XC,YC,label=("G"))
plt.plot(XD,YD,label=("D"))
plt.legend()
plt.show()


