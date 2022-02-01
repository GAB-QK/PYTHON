import matplotlib.pyplot as plt
def f(z,c):
    return z**2+c
# trace la trajectoire obtenue en appliaquant la fonciton f(z,c)
    #n fois d'affilé

def trajec (c,n):
    resultat=[0]
    for i in range(n):
        resultat.append(f(resultat[-1],c))
    return resultat
tr=trajec(0.01+0.5j,25)
X=[z.real for z in tr]
Y=[z.imag for z in tr]
plt.plot(X,Y,"bo-")
plt.show()





