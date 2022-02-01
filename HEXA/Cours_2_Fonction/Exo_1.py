'''exercice
ecriure unee fonction qui prend en parametre un nombre n
et qui renvoiee la liste de ses divisieurs pour savoir si a est un divisiseur de b on peut utiliserle modulo (%)
b%a==0'''


def modulo (n):
    valeur=[]
    for i in range(1,n+1):
        if n%i==0:
            valeur.append(i)
        else:
            continue
    return valeur
print(modulo(122))


