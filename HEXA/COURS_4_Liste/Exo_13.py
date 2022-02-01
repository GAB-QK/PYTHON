'''for element in [6,3,4,7]:
    print(element)


for i in range(len([6,3,4,7])):
    print (i)'''

def somme2(ls):
    resultat=0
    for valeur in ls:
        resultat+=valeur
    return resultat
print(somme2([6,3,4,7]))