import numpy as np

# on ouvre le fichier csv et on stocke les données dans un arrey
# skip_header permet de sauter la premiere ligne du fichier
a = np.genfromtxt("Classeur3.csv", delimiter=";", skip_header=1, dtype = int)
#print(a.ndim)
#print(a.shape)
b = np.genfromtxt("Classeur3.csv", delimiter=";", skip_header=1, dtype = int)
# on selectionne les colonnes de 5 à 9
a = a[:, 0:5]   # selectoin de toutes les lignes avec [:, et les collonnes de 5 à 9 avec 5:10]
b = b[:, 5:7]   # selection de toutes les lignes pour les étoiles
print(a.ndim)
print(a.shape)
print(a)
print(b)


