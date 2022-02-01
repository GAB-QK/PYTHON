'''exrcice
ecrire une fonction qui prend en parametre un nombre n  qui teste si n  est  premier
la fonction renvoi un booleen
rappel : n est premier s'il possède exactement deux diviseurs '''


def premier(n):
    BOO = False
    for i in range(1, n+1):
        if  i==n :
            continue
        if i==1:
            continue
        elif n%i != 0:
            BOO=True
        else:
            BOO=False
            break
    return BOO

print(premier(7))





