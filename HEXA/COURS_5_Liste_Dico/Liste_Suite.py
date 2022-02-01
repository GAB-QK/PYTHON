'''
liste=[3,5,1,7,3,2,9,4]
print(liste)
liste.sort()
print(liste)
'''

ls_non_trié=[3,5,1,7,3,2,9,4]

#FONCTION qui echange deselement d'indice i et j
#de la liste
def swap(liste,i,j):
    aux=liste[i]
    liste[i]=liste[j]
    liste[j]=aux
swap(ls_non_trié,1,5)

#tri par insetion
def tri_insert(liste):
    #print(liste)
    for i in range (1,len(liste)):
        j=i-1
        while j>=0 and liste[j+1]<liste[j]:
            swap(liste,j,j+1)
            j-=1
        #print(liste)
print("")

if __name__ == '__main__':

    print(ls_non_trié)
    liste1=ls_non_trié
    print(liste1)
    tri_insert(liste1)

#tri par selection
# on trouve la position de  valeur min
# on l'échange avec l'element de postion 0
# on trouve l'indice du minimum de l'indice restante
# on l'echange avec l'element de position 1

def tri_selection(liste):
    for i in range (0,len(liste)):
        L = liste[i:].index(min(liste[i:]))
        swap(liste,i,L+i)

nl = [31,6,38,17,64,100,4,45,21,54,33,12,45,23,1,45,12,45,23,4,25,67,45,45,85,35,76,34,67,32,78,90,12,45,32,6,43,75]
tri_selection(nl)
if __name__ == '__main__':
    print(nl)











