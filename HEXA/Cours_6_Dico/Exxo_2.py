'''exo
ecrire une fonction qui prend en parametre un dico
censé representer les notes des élèves ( les clés sont les noms et le valeurs sont les notes et
qui renvoie la liste des élèves qui ont la moyenne '''



def valide(notes):
    resultat=[]
    for cle in notes :
        if notes[cle] >= 10:
            resultat.append(cle)
    return resultat
liste= valide({"A":10,"B":12,"C":2})
print(liste)






