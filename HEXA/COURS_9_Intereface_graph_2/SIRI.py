import random
import numpy as np

class SIRI:
    def __init__(self,numero):
        self.numero=numero
    # methode qui prend en parametrel'etat de la grille
    # à un instant donne et renvoie un couple ligne collonne ou que l'IA veut jouer
    def joue(self,grille):
        pass

class SIRI_himar(SIRI):
    def __init__(self,numero):
        super().__init__(numero)

    def joue(self,grille):
        for i in range (3):
            for j in range(3):
                if grille [i,j]==0 :
                    return  (i,j)

class SIRI_Random(SIRI):
    def __init__(self,numero):
        super().__init__(numero)

    def joue(self,grille):
        i=random.randint(0,2)
        j= random.randint(0, 2)
        while grille[i,j] != 0:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
        return (i,j)

