import time,random,Liste_Suite

liste=[random.random() for i in range (5000)]

liste1=liste.copy()
t1=time.time()
Liste_Suite.tri_insert(liste1)
t2=time.time()
print("tri_insert",t2-t1)

liste2=liste.copy()
t1=time.time()
Liste_Suite.tri_insert(liste2)
t2=time.time()
print("tri_semction",t2-t1)

liste3=liste.copy()
t1=time.time()
liste3.sort()
t2=time.time()
print("sort :",t2-t1)


'''Exo
ecrire une fonction qui prend en rules une chaine de caratere ("insertion","selection" ou "sort")
et un nombre n 
et qui renvoiee le temps mis par l'algo choisit pour trier une liste random de taille n '''

def TRY (fonction,n):
    if fonction == "tri_insert":
        liste1 = liste.copy()
        t1 = time.time()
        Liste_Suite.tri_insert(liste1)
        t2 = time.time()
        print("tri_insert", t2 - t1)
    elif fonction == "tri_semction" :
        liste2 = liste.copy()
        t1 = time.time()
        Liste_Suite.tri_insert(liste2)
        t2 = time.time()
        print("tri_semction", t2 - t1)
    elif fonction == "sort :" :
        liste3 = liste.copy()
        t1 = time.time()
        liste3.sort()
        t2 = time.time()
        print("sort :", t2 - t1)

TRY("tri_semction",1100)







