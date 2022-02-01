import matplotlib.pyplot as plt
'''
Decouvertede matplotlit et
affichage de courberepresentative de fonctions'''
abscisse=[2, 4]
ordonnes=[5, 8]
#plt.plot(abscisse, ordonnes, "o-", markersize=10)

X = []
Y = []
'''
Afficher la courbe representative de f sur  l'intervalle [-5,5] avec suffisament de points
'''
'''
def f(x):
    return 2*x**2-7*x+1


for i in range(-50, 50):
    X.append(i/10)
    Y.append(f(i/10))
plt.plot(X, Y)
plt.show()
'''
'''ecxo
ecrire une fonction qui prend en parametre
2nombre a et b 
et qui affiche la courbe y=ax+b sur  l'intervalle [0;10] '''

def droite_affine(a,b):
    plt.plot([1,10],[b,a*10+b])

(droite_affine(4,9))
(droite_affine(-2,4))
(droite_affine(1,1))

plt.show()


